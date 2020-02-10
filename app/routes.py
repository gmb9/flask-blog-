#import certain functions into the global
#namespace
from app import app
from markdown import markdown
from flask import render_template, render_template_string, request, session
from app.blog_helpers import render_markdown
import os

#safe global import (okay to use)
import flask

#global import (try to avoid)
#from flask import *

#home page
@app.route("/")
@app.route("/index")
def home():
    return render_markdown('index.md')

@app.route('/all')
def all():
    #TODO: figure out how to find all files 
    #in the app
    view_data = {}
    view_data["pages"] = os.listdir(r"C:\Users\gmbec\OneDrive\Desktop\flaskblogcurrent\flask-blog-\app\templates")


    #view_data["pages"] = ([ #parens allows for multi
    #                        #line statements in Py
    #    'about.html',
    #    'test.html',
    #    'foo.html'
    #])
    return render_template("all.html", data = view_data)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['user_name']
        password = request.form['password']

        if(username == "") or (password == ""):
            return render_template('login.html')
        else:
            session['user_name'] = username
            session['password'] = password
            return render_markdown('index.md')
    else:
        return render_template('login.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        if (len(session['user_name']) > 0) and (session['password'] == app.config['ADMIN_PASSWORD']):
            return render_template('login.html')
    else:
        return render_template('edit.html')

@app.route("/favicon.ico")
def favicon():
    return ""

@app.route("/click_tracker", methods=['GET', 'POST'])
def click_tracker():
    view_data = {}
    view_data["click_count"] = 0
    if request.method == 'POST':
        view_data["click_count"] = request.values["click_count"]
        view_data["click_count"] = int(view_data["click_count"]) + 1
    return render_template('click_tracker.html', data=view_data)
    

#generic page
@app.route("/<view_name>.md")

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.md')
    #view_data = {} #create empty dictionary
    return render_template_string(html)

@app.route("/<view_name>.html")
#input parameter name must match route parameter
def render_page_html(view_name):
    html = (view_name + '.html')
    view_data = {} #create empty dictionary
    view_data["click_count"] = 0
    return render_template(html, data = view_data)