from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def index():
    flash("Thank you for using Flask to display this message.")
    print("You're using the index.html here")
    return render_template("index.html")

@app.route("/about")
def about():
    flash("Thanks for visiting")
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)