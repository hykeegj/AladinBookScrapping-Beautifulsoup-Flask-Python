import csv


def save_to_file(book_list):
    file = open('books.csv', mode='w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["tag", "title", "price"])

    for book in book_list:
        writer.writerow(book.values())
    return
