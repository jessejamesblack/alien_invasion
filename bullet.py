import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	# a class to manage bullets fired from the ship

	def __init__(self, ai_settings, screen, ship):
		# create a bullet object at the ships current pos
		super(Bullet, self).__init__()
		self.screen = screen

		# create a bullet
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# store the bullet pos
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		# move the bullet up the screen
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		# draw the bullet to the screen
		pygame.draw.rect(self.screen, self.color, self.rect)