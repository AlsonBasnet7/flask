from flask import Flask, render_templates, request

app =Flask(__name__)

# @app.route("/")
# def index():
#     return render_templates("index.html")
@app.route("/predict", methods=["GET","POST"])
def login():
    if request.method=="POST":
     email= request.form('email')
     password= request.form('passowrd')
     if email =="admin@gmail.com" and password =="1234":
        return "<h2 sytle='color:green'>Login Successful</h2>"
     else:
        return "<h2 sytle='color:green'>Invalid Credentials</h2>"
     return "Thanks for using my system."
    return render_templates("index.html")

app.run(debug=True)