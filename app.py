from flask import Flask, render_template,request,redirect


app = Flask(__name__)

tasks = [
    {"name":"レポート書く","done":False},
    {"name":"買い物に行く","done":False},
    {"name":"Pythonの勉強","done":False}
]

@app.route("/")
def home():
    return render_template("index.html", tasks = tasks)

@app.route("/add", methods = ["POST"])
def add():
    new_task = request.form["new_task"]
    tasks.append(new_task)
    return redirect("/")

@app.route("/done/<int:task_id>")
def done(task_id):
    tasks[task_id]["done"] = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)