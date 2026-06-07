from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    # These are the values that i am passing in my HTML file. So basically 
    # Jinja works like a templating engine in your system. 
    name= "Alson Basnet"
    language="Python"
    itemstored=[1,2,3,4,5]
    footer="<p>Copyrights 2026 | All rights reserved</p>"
    return render_template("index.html",name= name,language=language,itemstored=itemstored,footer=footer)
app.run(debug=True)     