class GameStats():
	# track stas for alien invasion

	def __init__(self, ai_settings):
		# init
		self.ai_settings = ai_settings
		self.reset_stats()

		# start alien invasion
		self.game_active = True

	def reset_stats(self):
		# init stats that change during game play
		self.ships_left = self.ai_settings.ship_limit