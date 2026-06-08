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


## Day 04

Temlpate inheritance is basically the base template that other templates can extend.

Message flashing in Flask 
Flashing is a way to send temporary messages from backend to the frontend.
 
 These messages we generally use for:


 *Status updates
 <br>
 *Error messages
 <br>
 *Notification 
 

