from steimatzky import *

scraper = SteimatzkyScraper()

wimpy_kid_books = scraper.search_for_items('יומנו של חנון')

for wimpy_kid_book in wimpy_kid_books:
    print('Title: ' + wimpy_kid_book.title)
    print('Author: '+ wimpy_kid_book.author.name)
    print(wimpy_kid_book.get_more_info().description)
    print('')