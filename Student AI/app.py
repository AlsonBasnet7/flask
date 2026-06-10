from flask import Flask, render_template, request, flash, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-in-production")

students = [
    {"id": 1, "name": "John Doe", "marks": 85, "prediction": "Excellent"},
    {"id": 2, "name": "Alice Smith", "marks": 65, "prediction": "Good"},
    {"id": 3, "name": "Bob Rajan", "marks": 45, "prediction": "Needs Improvement"},
]


def get_prediction(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 60:
        return "Good"
    else:
        return "Needs Improvement"


@app.route("/")
def home():
    return render_template("home.html", total=len(students))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if username == "admin" and password == "1234":
            session["logged_in"] = True
            flash("Welcome back, admin!", "success")
            return redirect("/")
        else:
            flash("Invalid username or password.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect("/login")


@app.route("/students")
def students_page():
    return render_template("students.html", students=students)


@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        marks_raw = request.form.get("marks", "")

        if not name:
            flash("Student name is required.", "error")
            return render_template("add_student.html")

        try:
            marks = int(marks_raw)
            if not (0 <= marks <= 100):
                raise ValueError
        except ValueError:
            flash("Marks must be a number between 0 and 100.", "error")
            return render_template("add_student.html")

        student = {
            "id": len(students) + 1,
            "name": name,
            "marks": marks,
            "prediction": get_prediction(marks),
        }
        students.append(student)
        flash(f"{name} added successfully.", "success")
        return redirect("/students")

    return render_template("add_student.html")


@app.route("/student/<int:id>")
def student_detail(id):
    selected = next((s for s in students if s["id"] == id), None)
    if selected is None:
        flash("Student not found.", "error")
        return redirect("/students")
    return render_template("student_detail.html", student=selected)


@app.route("/search")
def search():
    grade = request.args.get("grade", "").upper()
    result = []
    for student in students:
        if grade == "A" and student["marks"] >= 80:
            result.append(student)
        elif grade == "B" and 60 <= student["marks"] < 80:
            result.append(student)
        elif grade == "C" and student["marks"] < 60:
            result.append(student)
    return render_template("students.html", students=result, search_grade=grade)


if __name__ == "__main__":
    app.run(debug=True)
