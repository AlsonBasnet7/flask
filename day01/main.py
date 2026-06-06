from flask import Flask, render_template

app = Flask(__name__, static_folder='assets',)

@app.route("/")
def display():
    return "I am checking wheather i can run this main.py app in the local host or not"
@app.route("/home")
def home():
    return "Hey, this is the home section."
@app.route("/contact")
def contact():
    return render_template("index.html")
@app.route("/about")
def about():
    return "Hey this is the about section of the code base!"

if __name__ == "__main__":
    app.run(debug=True)