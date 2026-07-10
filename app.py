from flask import Flask, render_template, request

app = Flask(__name__)

students_list = []


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/students/add", methods=["GET", "POST"])
def add_student():
    if request.method == 'POST':
        name = request.form["name"]
        year_group = request.form["year_group"]
        exam_board = request.form["exam_board"]
        grade = request.form["grade"]

        student = {
            "name": name,
            "year_group": year_group,
            "exam_board": exam_board,
            "grade": grade
        }

        students_list.append(student)

        print(students_list)

    return render_template("add_student.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)




