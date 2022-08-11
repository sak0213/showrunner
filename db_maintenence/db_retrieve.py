from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
collection = client['showrunner_db']['events']

results = collection.aggregate([{
    "$group" :
        {"_id" : "$event_venue",
         "events":{"$sum" : 1}}}
])

for i in results:
    print(i)
