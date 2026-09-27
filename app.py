from flask import Flask, render_template,request,redirect
import sqlite3


app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks = tasks)

@app.route("/add", methods = ["POST"])
def add():
    new_task = request.form["new_task"]
    conn = get_connection()
    conn.execute("INSERT INTO tasks (name,done) VALUES (?,0)", (new_task,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/done/<int:task_id>")
def done(task_id):
    conn = get_connection()
    conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)