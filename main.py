from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


@app.route("/read")
def read_main():
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM discord")
    List = cursor.fetchall()
    return render_template("read_main.html", List=List)


@app.route("/read/<int:id>")
def read_id(id):
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM discord")
    element = cursor.fetchall()[int(id)]
    return render_template("read_id.html", element=element)


@app.route("/add", methods=["POST"])
def add():
    body = request.json
    player_1 = body["player_1"]
    player_2 = body["player_2"]
    id = body["id"]
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO discord VALUES({id}, '{player_1}', '{player_2}')")
    db.commit()
    return render_template("add.html")


@app.route("/delete")
def delete_main():
    return "Введите индес ячейки для удаления"


@app.route("/delete/<int:index>", methods=["DELETE"])
def delete(index):
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM discord WHERE id = ?", (index,))
    db.commit()

    return "Успешно удалилось"


@app.route("/update")
def update_main():
    return "Введите id player_1 player_2"


@app.route("/update/<int:index>", methods=["PUT", "GET"])
def update(index):
    body = request.json
    player_1 = body["player_1"]
    player_2 = body["player_2"]
    db = sqlite3.connect("discord.db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE discord SET player_1 = '{player_1}', player_2 = '{player_2}' WHERE id = {index}")
    db.commit()
    cursor.execute(f"SELECT * FROM discord WHERE id = {index}")
    element = cursor.fetchall()
    return render_template("update.html", element=element)


if __name__ == "__main__":
    app.run()

