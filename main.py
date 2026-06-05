from flask import Flask

app = Flask(__name__)

@app.route("/")
def display():
    return "I am checking wheather i can run this main.py app in the local host or not"
@app.route("/home")
def home():
    return "Hey, this is the home section."
@app.route("/contact")
def contact():
    return "Hey! This is the contact section of the code!"

if __name__ == "__main__":
    app.run(debug=True)