class GameStats():
	# track stas for alien invasion

	def __init__(self, ai_settings):
		# init
		self.ai_settings = ai_settings
		self.reset_stats()

		# start game inactive
		self.game_active = False

		self.high_score = 0

	def reset_stats(self):
		# init stats that change during game play
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1