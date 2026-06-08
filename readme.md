# I'm Learning Flask

---

## Day 01

I learning what is flask why is it necessary for the web developers.  
Also did a demo on how flask operates.  
Wrote some function to understand the working flow of the flask.  
Hosted some function in the Local host.

---

## Day 02

Static and templates folder in the flask.

Static folder we generally store the JS, CSS, etc file here. We can create the static path of any folder.  
Templated folder is where the HTML files goes.

Form handling learned about render_templates, request, GET and POST.  
Generally i understood how can i access files from the folders.

Also did work on mini login system.

---

## Day 03

Jinja Templates in flask

Jinja2, i am currently using this.  
Jinja2 is the templating engine used by flask.  
It allows us to embed python code like logic inside our HTML.

- Display variable (like models predictions or user inputs)  
- Loop through lists (Like rows in a data engine)  
- Use conditions (Like showing a message only when needed)

render_template -> to pass variables form flask to HTML  
{{xyz}} -> to display the data  
{%....%} -> to control structures like loops and conditions  

Overall, Jinja makes it easy to combine logic and layout for dynamic pages.


## Day 03

Temlpate inheritance is basically the base template that other templates can extend.

Message flashing in Flask 
What Is Flashing?
Flashing is a way to send temporary messages from the backend (Flask) to the frontend (HTML). These messages are usually used for:

Status updates (e.g., "Prediction complete")
Error messages (e.g., "Invalid input")
Notifications (e.g., "File uploaded successfully")
Flashed messages are stored in the session and automatically cleared after being displayed.

Step 1: Set a Secret Key
Flashing uses Flask's session, so you must set a secret key:

from flask import Flask
 
app = Flask(__name__)
app.secret_key = 'your_secret_key'

Step 2: Flash a Message in Your Route
Use flash() to send a message:

from flask import flash, redirect, render_template, request
 
@app.route('/predict', methods=['POST'])
def predict():
    feature = request.form.get('feature1')
    if not feature:
        flash('Please enter a value')
        return redirect('/')
    
    # process prediction here
    flash('Prediction complete')
    return redirect('/')

flash('message') stores the message
redirect('/') sends the user back to a route where the message will be displayed
Step 3: Display Flashed Messages in the Template
In your base or main template (e.g. index.html or base.html):

{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>
      {% for msg in messages %}
        <li>{{ msg }}</li>
      {% endfor %}
    </ul>
  {% endif %}
{% endwith %}

This block retrieves all flashed messages and displays them in a list. You can style them with CSS as needed.

Summary
Use flash('your message') to send a message
Use get_flashed_messages() in your template to retrieve and display them
Useful for alerts, validation feedback, and user notifications