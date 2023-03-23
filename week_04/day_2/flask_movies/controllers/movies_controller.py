from flask import *
from app import app
from models.movie_list import *
from models.movie import *


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/movies")
def movies_list():
    return render_template("index.html", 
                           title = 'Movies', 
                           movie_list= movie_list
                           )

@app.route("/movies/<index>")
def movies_show(index):
    return render_template("show.html", 
                           title = 'Movies', 
                           solo_movie = movie_list[int(index)])

                           