# import pymongo
from venues.mr_smalls import mrsmalls

# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# db = client.showrunner_db
# collection = db.events

venues = [mrsmalls]
for venue in venues:
    for event in venue():
        print(event)


