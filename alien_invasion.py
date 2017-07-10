import pygame

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
	ship = Ship(screen)

	# start the main loop for the game
	while True:
		# check for keyboard presses or mouse movements and redraw
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)

run_game()