from flask import Flask, render_template, request
app =Flask(__name__)

@app.route("/")
# def index():
#     return render_template("index.html")
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
      email= request.form["email"]
      password= request.form["password"]
      print(f"The name is {email} and the password is {password}")
      if email =="admin@gmail.com" and password =="1234":
       return "<h2 style='color:green'>Login Successful</h2>"
      else:
        return "<h2 style='color:green'>Invalid Credentials</h2>"
      return "Thanks for using my system."
    return render_template("index.html")

app.run(debug=True)