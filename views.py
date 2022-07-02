from flask import Blueprint
#blueprint of our application; it has a bunch of views/url's inside it
views = Blueprint('views', '__name__') #defines blueprint

@views.route('/')  #decorator
def home():
    return "<h1>hello world </h1>"

#this function will run whenever we go to the url/route