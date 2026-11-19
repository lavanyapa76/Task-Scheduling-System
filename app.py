from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, add_task, get_tasks, get_workers
from scheduler import start_scheduler

app = Flask(__name__)
app.secret_key = "task-scheduler-demo-key"

init_db()
start_scheduler()

@app.route("/")
def home():
    return render_template("index.html", tasks=get_tasks(), workers=get_workers())

@app.route("/add", methods=["POST"])
def add():
    task_name = request.form.get("task_name", "").strip()
    if task_name:
        add_task(task_name)
        flash("Task submitted successfully!")
    else:
        flash("Please enter a task name.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
