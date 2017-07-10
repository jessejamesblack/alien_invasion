import pygame

class Ship():

	def __init__(self, screen):
		# init ship and set pos

		self.screen = screen

		# load the ship image and get its rect.

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start each ship at the bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		# draw the ship
		self.screen.blit(self.image, self.rect)