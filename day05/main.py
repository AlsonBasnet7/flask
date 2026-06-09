from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'
#guery parameters and api creation 

@app.route("/")
def system():
     return "The system is running"
@app.route("/index")
def index():
    # we can also give the default value of the query parameters.
    # name=request.args.get("name" defualt=undefined)
    name = request.args.get("name")
    language = request.args.get("language")
    print (name, language)
    return render_template("index.html",name=name, language=language) 

app.run(debug=True)