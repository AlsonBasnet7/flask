from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

#home section 
@app.route("/")
def home():
    return render_template("home.html")

#login section 
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method=="POST":
        email=request.form["email"]
        password= request.form["password"]
    return render_template("login.html")

#contact section
@app.route("/contact")
def  contact():
    return render_template("contact.html")

#projects section 
@app.route("/projects")
def projects():
    return render_template("projects.html")

#projects_details 
@app.route("/projects_details")
def projects_details():
    return render_template("projects_details.html")

if __name__ == "__main__":
    app.run(debug=True)



