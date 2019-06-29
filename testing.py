from steimatzky import *
import csv


scraper = SteimatzkyScraper()

csvwriter = csv.writer(open('Best Selling Fiction Books in Israel.csv', 'w'))
csvwriter.writerow(['כותרת', 'נכתב על ידי', 'קטגוריה'])


def write_list_of_bestsellers(bestsellers, category):
    global csvwriter
    for best_seller in bestsellers:
        csvwriter.writerow([best_seller.title, best_seller.author.name, category])

write_list_of_bestsellers(
    scraper.get_bestsellers_by_genre(BestSellerBookType.fiction),
    'סיפורת'
)

write_list_of_bestsellers(
    scraper.get_bestsellers_by_genre(BestSellerBookType.childrens),
    'ילדים ונוער'
)

write_list_of_bestsellers(
    scraper.get_bestsellers_by_genre(BestSellerBookType.non_fiction),
    'עיון'
)
