from flask import Blueprint
from flask import Flask, redirect, url_for, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route("/")
def welcome():
	#if current_user.is_authenticated:
		#return "<h1>Welcome to Online Class<h1>"
	return render_template("index.html")

@views.route("/home")
@login_required
def home():
	return "<h1>Welcome to Online Class<h1>"