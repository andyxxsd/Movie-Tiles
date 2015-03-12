'''
	Modified from fresh_tomatoes.py.
	The logic stays same but I customized more feature.
	+   Read template from file
	+   Extended information for movies
'''

import webbrowser
import os

# Styles and scripting for the page
main_page = open("template.html", 'r').read()
main_page_head = open("head.html", 'r').read()

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-url="{trailer_url}" data-toggle="modal" data-target="#trailer">
	<img src="{poster_image_url}" width="220" height="342">
	<h2><span class="movie-title">{movie_title}</span></h2>
	<small>directed by <strong><span class="movie-director">{movie_director}</span></strong></small>
	<span class="genre hide">{genre}</span>
	<span class="release-date hide">{release_date}</span>
	<span class="description hide">{description}</span>
	<span class="movie-writers hide">{movie_writers}</span>
	<span class="movie-stars hide">{movie_stars}</span>
</div>
'''


def create_movie_tiles_content(movies):
	# The HTML content for this section of the page
	content = ''
	for movie in movies:
		# Render the movies information into HTML labels and attributes.
		content += movie_tile_content.format(
			movie_title=movie.title,
			movie_director=', '.join(movie.director),
			movie_writers=', '.join(movie.writers),
			movie_stars=', '.join(movie.stars),
			description=movie.storyline,
			release_date=movie.release_date.strftime("%d %b %Y")+" (USA)",
			genre='.'.join(movie.genre),
			poster_image_url=movie.poster_url,
			trailer_url=movie.trailer_url
		)
	return content


def open_movies_page(movies):
	# Create or overwrite the output file
	output_file = open('index.html', 'w')

	# Replace the placeholder for the movie tiles with the actual dynamically generated content
	rendered_content = main_page.format(movie_tiles=create_movie_tiles_content(movies))

	# Output the file
	output_file.write(main_page_head + rendered_content)
	output_file.close()

	# open the output file in the browser
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
