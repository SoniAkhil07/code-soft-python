from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Task:
    def __init__(self, text, id):
        self.text = text
        self.id = id


tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_text = request.form.get('task')
        tasks.append(Task(task_text, len(tasks) + 1))  # Assign unique IDs
    return render_template('index.html', tasks=tasks)


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if index-1>= 0 and index-1 < len(tasks):
        if request.method == 'POST':
            edited_task_text = request.form.get('editedTask')
            tasks[index - 1].text = edited_task_text  # Adjust index
            return redirect('/')
        return render_template('edit.html', task=tasks[index - 1], index=index)
    else:
        return "Invalid task index."

@app.route('/delete/<int:index>')
def delete_task(index):
    tasks.pop(index - 1)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
