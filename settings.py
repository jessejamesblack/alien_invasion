class Settings():
	# Settings for alien invasion

	def __init__(self):
		# intialize
		# screen
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# ship
		self.ship_speed_factor = 1.5

		# missiles
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		# alien
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1