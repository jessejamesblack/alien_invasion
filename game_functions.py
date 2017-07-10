import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
	# keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		# right movement
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		# check for contious movement
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
	
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right += True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
	# update images on screen and flip new screen
	screen.fill(ai_settings.bg_color)

	# draw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()

	# make the most recently drawn screen visible
	pygame.display.flip()

def update_bullets(bullets):
	# update pos of bullets and remove old ones
	bullets.update()
	# delete old bullets and free memory
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
	# create new bullet and add to group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)