import sys
import pygame

def check_events():
	# keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
	

def update_screen(ai_settings, screen, ship):
	# update images on screen and flip new screen
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# make the most recently drawn screen visible
	pygame.display.flip()