from flask import Blueprint, render_template, request
import urllib
import json

views = Blueprint('views', __name__)

@views.route("/")
def home():
    print("HELLO I AM A FLASK APP")
    return render_template("home.html" , page_name = "WHAT2WATCH")


# @views.route("/search/<string:movieName>")
# def search_results(movieName):
#     url =  f"http://www.omdbapi.com/?s={movieName}&apikey=205f2fa0"
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     jsonData = json.loads(data)["Search"]
#     return render_template("home.html" , page_name = "SEARCH RESULTS" , movieList = jsonData)


@views.route("/search" , methods = ['GET'])
# GET  - Insecure ( Search )
# POST - Secure (Password , Credit Number )
def search_results():
    movieName  =  request.args.get("Moviequery")
    try:
        url =  f"http://www.omdbapi.com/?s={movieName}&apikey=205f2fa0"
        url = url.replace(" ", "%20")
        response = urllib.request.urlopen(url)
        data = response.read()
        jsonData = json.loads(data)["Search"]
        return render_template("home.html" , page_name = "SEARCH RESULTS" , movieList = jsonData , query = movieName)
    except Exception as e:
        print(e)
        return f"NO INTERNET CONNECTION {e}"


