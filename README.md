# wikipedia-plot-scraper

This script allows you to strip the plots of books/movies from Wikipedia articles and saves them as seperate text files.\n
\n
It's a work in progress, so far it works on articles that have "Plot\[edit\]" explicitly mentioned, however, if there are other words in the "Plot" heading (e.g. "Plot Synopsis\[edit\]" or "Plot Summary\[edit\], it will not work. I'm working on ironing out the kinks.\n
\n
Make sure you install the following libraries:\n
```{python}
pip install urllib.request
pip install bs4
```
