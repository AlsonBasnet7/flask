from flask import Flask ,render_template, request

app=Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def display():
    return "This is the main.py code file"
@app.route("/index")
def index():
    name= request.args.get("name")
    lang=request.args.get("lang")
    return render_template("index.html", name=name, lang= lang)
if __name__ == "__main__":
    app.run(debug=True)