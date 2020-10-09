from flask import Flask, render_template, request, redirect, send_file
from aladin import extract
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        exisitingBooks = db.get(word)
        if exisitingBooks:
            books = exisitingBooks
        else:
            books = extract(word)
            db[word] = books
    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(books),
                           books=books)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()

        word = word.lower()

        books = db.get(word)
        if not books:
            raise Exception()

        save_to_file(books)

        return send_file("books.csv", attachment_filename='books.csv')
    except:
        return redirect("/")


app.run(host="127.0.0.1")
