from pprint import pprint
import json
from pymongo import MongoClient

dbClient = MongoClient("mongodb+srv://shivanshkothari2004:Shivansh%402004@myvedicjourney.rhzuxul.mongodb.net/?retryWrites=true&w=majority&appName=MyVedicJourney")
siteDB = dbClient["siteData"]

# for doc in siteDB.blogdatas.find({}, {"_id" : 0, "firstName": 1, "lastName": 1, "email" : 1, "password" : 1}):
for doc in siteDB.blogdatas.find({}, {"_id" : 0, "heading": 1, "url": 1, "image_path" : 1, "post_text" : 1}):
    print(doc)