from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def getScrape():
    mars = mongo.db.mars
    marsData = scrape_mars.scrape_all()
    mars.update({},marsData, upset=True)
    return "Scraping Successful"

    if __name__=="__main__":
        app.run()