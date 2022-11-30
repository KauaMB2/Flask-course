from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'
#http://127.0.0.1:5000/
