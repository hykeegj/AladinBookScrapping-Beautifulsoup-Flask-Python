import csv


def save_to_file(book_list):
    file = open('title.csv', mode='w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["tag", "title", "price"])

    for item in book_list:
        writer.writerow([item[0], item[1], item[2]])
    return
