from flask import Flask, render_template, request,flash, redirect
app = Flask(__name__)
app.secret_key = 'your_secret_key'

#this is kinda like a data base to the system i am creating
students = [
    {
        "id":1,
        "name":"John",
        "marks":85
    },
    {
        "id":2,
        "name":"Alice",
        "marks":65
    }
]


#home section 
@app.route("/")
def home():
    return render_template("home.html")

#login section 
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            flash("Login Successful")
            return redirect("/")
        else:
            flash("Invalid Credentials")

    return render_template("login.html")

# students details section
@app.route("/details/<int:id>")
def  stundet_details():
    selected_student=None
    for student in students:
        if student["id"]==id:
            selected_student=student
    
    return render_template("contact.html",student=selected_student)

#students section  to view student present in the systm
@app.route("/students")
def projects():

    return render_template("students.html", students=students)

#add students
@app.route("/addstudents", methods=["GET","POST"])
def projects_details():
    if request.method=="POST":
        name= request.form.get("name")
        marks= int(request.form.get("marks"))
        if marks>=80:
            prediction ="Excellent"
        elif marks >=60:
            prediction="Good"
        else:
            prediction="Needs Improvement"
        student={
            "id":len(students)+1,
            "name":name,
            "marks":marks,
            "prediction":prediction
        }
        students.append(student)
        flash("Students added successfully")
        return redirect("/students")
    
    return render_template("add_students.html")

#this is to search the students present in the dataset.
@app.route("/search")
def search():

    grade = request.args.get("grade")

    result = []

    for student in students:

        if grade == "A" and student["marks"] >= 80:
            result.append(student)

        elif grade == "B" and student["marks"] >= 60:
            result.append(student)

    return render_template(
        "students.html",
        students=result
    )
if __name__ == "__main__":
    app.run(debug=True)



