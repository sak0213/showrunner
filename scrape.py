import pymongo
from venue_classes.all_venues import venue_list


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.showrunner_db
collection = db.events




# FULL RUN OF LIST
for venue in venue_list.values():
    for event in venue().get_events():
        collection.insert_one(event.event_output())


