from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/students/add")
def add_student():
    return render_template("add_student.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)




