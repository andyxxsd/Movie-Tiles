from pyquery import PyQuery as pq
from module import Movie
import re
from datetime import datetime


def crawl(urls=[], debug=False):
	def ugly_parse(parse):
		arr = d(parse)
		item = []
		for val in arr:
			item.append(pq(val).html().strip())
		return item

	movies = []
	for url in urls:
		if debug:
			print("Processing url =", url)
		d = pq(url)
		res = {"release_date": datetime.strptime(d(".infobar meta[itemprop='datePublished']").attr('content'), "%Y-%m-%d"),
			   "title": ugly_parse(".header [itemprop='name']")[0],
			   "director": ugly_parse("div[itemprop='director'] [itemprop='name']"),
			   "writers": ugly_parse("div[itemprop='creator'] [itemprop='name']"),
			   "stars": ugly_parse("div[itemprop='actors'] [itemprop='name']"),
			   "storyline": ugly_parse("p[itemprop='description']")[0],
			   "poster_url": d("#img_primary img[itemprop='image']").attr('src'),
			   "trailer_url": re.search(r"(.+)/\?", "http://www.imdb.com" + d("[itemprop='trailer']").attr('href')).group(1),
			   "genre": ugly_parse(".infobar [itemprop='genre']")
		}
		movies.append(Movie(res))
		if debug:
			print(res)
	return movies