from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   mars_hemi = mongo.db.mars_hemi.find_one()
   return render_template("index.html", mars=mars, mars_hemi=mars_hemi)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_hemi = mongo.db.mars_hemi
   mars_data, mars_hemi_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   hars_hemi.update({}, mars_hemi_data, upsert=True)
   return "Scraping Successful!"   

if __name__ == "__main__":
   app.run()  