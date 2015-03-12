'''
	Movie module for the concept of OOP.
'''


class Basic():
	def __init__(self, title):
		self.title = title


class Movie(Basic):
	"""docstring for Movie"""
	def __init__(self, info):
		super(Movie, self).__init__(info["title"])
		self.release_date = info["release_date"]
		self.director = info["director"]
		self.stars = info["stars"]
		self.writers = info["writers"]
		self.storyline = info["storyline"]
		self.poster_url = info["poster_url"]
		self.trailer_url = info["trailer_url"]
		self.genre = info["genre"]

	def __str__(self):
		return self.title + " directed by " + (len(self.director)>1 and self.director.__str__() or self.director[0])