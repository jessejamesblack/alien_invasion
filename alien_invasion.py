import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# intialize game and create a screen object and settings
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Alien Invasion")

	# sets background color
	bg_color = (230, 230, 230)

	# make ship
	ship = Ship(ai_settings, screen)
	# make a group to store bullets in
	bullets = Group()

	# start the main loop for the game
	while True:
		# check for keyboard presses or mouse movements and redraw
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)

		
		#print(len(bullets))

run_game()