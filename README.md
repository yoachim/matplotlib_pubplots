# matplotlib_pubplots

Overview
--------
I really hate how plots that look good in papers look terrible when projected on powerpoint slides.  I'd like to make a simple matplotlib function that can be used to generate different versions of a plot.  The idea is that you write a python function that makes a plot. Pass that plot to the wrapper, and it will call your plotting function numerous times, changing the matplotlib default settings appropriately. Plan to make plots that are optimized for "publication_two_column", "publication_one_column", "powerpoint", and "web thumbnail".


Relevant Links:
https://github.com/olgabot/prettyplotlib
https://github.com/daler/matplotlibrc
http://python4mpia.github.io/plotting/publication.html
https://aas.org/authors/graphics-guidelines


Fuck, I'm kinda re-inventing matplotlib style sheets:
http://matplotlib.org/users/style_sheets.html

