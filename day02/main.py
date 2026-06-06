from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predit', methods=['POST'])
def predict():
    value = request.form['feature1']
    return f"received input:{value}"

