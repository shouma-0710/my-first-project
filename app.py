from flask import Flask, render_template,request,redirect


app = Flask(__name__)

tasks = ["レポートを書く", "買い物に行く", "Pythonの勉強"]


@app.route("/")
def home():
    return render_template("index.html", tasks = tasks)

@app.route("/add", methods = ["POST"])
def add():
    new_task = request.form["new_task"]
    tasks.append(new_task)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)