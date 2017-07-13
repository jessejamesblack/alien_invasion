import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
	# keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

		# right movement
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		# check for contious movement
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# reset game settings
		ai_settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True

		# reset the sb
		sb.prep_score()
		sb.prep_high_score()
		sb.level()
		sb.prep_ships()

		# empty the lists
		aliens.empty()
		bullets.empty()

		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship
			
	
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right += True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, stats, sb, aliens, bullets, play_button):
	# update images on screen and flip new screen
	screen.fill(ai_settings.bg_color)

	# draw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)

	# draw score stuff
	sb.show_score()

	# draw play button if game is inactive
	if not stats.game_active:
		play_button.draw_button()

	# make the most recently drawn screen visible
	pygame.display.flip()

def update_bullets(ai_settings, screen, ship ,aliens, bullets):
	# update pos of bullets and remove old ones
	bullets.update()
	# delete old bullets and free memory
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	# check for bullet/alien collisions
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
	
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# remove bullets and aliens that have collided
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	if len(aliens) == 0:
		#destroy existing bullets and create new fleet and speed up game
		bullets.empty()
		ai_settings.increase_speed()
		# increase level
		stats.level += 1
		sb.prep_level() 

		create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
	# create new bullet and add to group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
	# finds the number of aliens in a row
	avaliable_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(avaliable_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	# find number of rows
	avaliable_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(avaliable_space_y / (2 * alien_height))
	return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
# create an alien and place it in a row
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	alien.rect.x = alien.x
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	# create an alien then do math to find aliens in row
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	
	# create rows of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# covers ship being hit
	if stats.ships_left > 0:
		# decrement lives
		stats.ships_left -= 1

		# update sb
		sb.prep_ships()

		# empty alien and bullet list
		aliens.empty()
		bullets.empty()

		# create a new fleet and ship
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		sleep(0.5)

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# update pos of all aliens in the fleet
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# if the ship and aliens collide end game
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

	# look for aliens at the bottom of the screen
	check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
	# self explaintory
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	# drop and change direction
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
	
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			break

def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()