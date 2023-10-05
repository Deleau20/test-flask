from flask import Flask, render_template, request, redirect, url_for
from classe import Student

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("nom")
        year = request.form.get("age")
        classe = request.form.get("classe")
        user = Student()
        user.add_student(name, year, classe)
        print(f"nom: {name}, age: {year}, classe: {classe}")
        return redirect(url_for("student"))
    return render_template("index.html")

@app.route('/students')
def student():
    user = Student()
    # data = user.get_all_student()
    # for i in data:
    #     print(i)
    return render_template("list.html", students=user.get_all_student())

@app.route('/students/<int:id>')
def get_students(id):
    return f"""<h2>Je suis l'élève {id}: </h3>"""


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = Student()
    student = user.get_student(id)

    if not student:
        return redirect(url_for('student'))

    if request.method == 'POST':
        name = request.form.get("nom")
        year = request.form.get("age")
        classe = request.form.get("classe")
        user.update(id,name,year,classe)
        return redirect(url_for('student'))
    return render_template("update.html", student = student)