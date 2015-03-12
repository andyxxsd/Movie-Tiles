__author__ = 'skylarzheng'
'''
	Static movie trailer website assemble procedure:
		1.  Select movies. Then wrote their IMDB home page links into movie_url.py
		2.  Crawl information from IMDB.
		3.  Render HTML. (To file index.html)
		4.  Your webbrowser will pop up and display the website.
'''

from src.crawler import crawl
from movie_url import urls
from src.html_render import *

movies = crawl(urls, True)
open_movies_page(movies)
print("Done")