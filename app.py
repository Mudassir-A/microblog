import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("localhost", 27017)
app.db = client.microblog
entries = []


@app.route("/", methods=["GET", "POST"])
def home():


    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    entries_with_date = [
        (
            entry["content"],
            entry["date"],
        )
        for entry in app.db.entries.find({})
    ]

    data = [entry for entry in app.db.entries.find({})]
    print(data)
    return render_template("home.html", entries=entries_with_date)
