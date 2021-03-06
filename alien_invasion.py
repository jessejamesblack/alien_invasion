import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
	# intialize game and create a screen object and settings
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Alien Invasion")

	# play button
	play_button = Button(ai_settings, screen, "Play")

	# instance for game stats and score
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	# sets background color
	bg_color = (230, 230, 230)

	# make ship
	ship = Ship(ai_settings, screen)
	# make a group to store bullets in
	bullets = Group()
	aliens = Group()

	# make aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# start the main loop for the game
	while True:
		# check for keyboard presses or mouse movements and redraw
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)


		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		#print(len(bullets))

run_game()