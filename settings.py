class Settings():
	# Settings for alien invasion

	def __init__(self):
		# intialize
		# screen
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# ship
		self.ship_limit = 3

		# missiles
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		# alien
		self.fleet_drop_speed = 10

		self.speedup_scale = 1.1
		
		self.score_scale = 1.5

		self.intialize_dynamic_settings()

	def intialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.fleet_direction = 1

		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.fleet_direction *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)