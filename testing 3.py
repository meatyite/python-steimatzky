from steimatzky import SteimatzkyScraper

scraper = SteimatzkyScraper()

author = scraper.search_for_items('James Patterson')[0].author

books = author.get_books()
for book in books:
    print(book.title)