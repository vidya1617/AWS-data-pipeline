from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # Store tasks in a simple list

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")  # Get the task from the form
        if task:  # Ensure the task is not empty
            tasks.append(task)
        return redirect("/")  # Redirect to the same page after adding a task
    # Pass the enumerated tasks to the template
    return render_template("index.html", tasks=enumerate(tasks))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):  # Ensure the task_id is valid
        tasks.pop(task_id)  # Remove the task by its index
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
