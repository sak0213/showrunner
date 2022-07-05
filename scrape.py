# import pymongo
from venue_classes.all_venues import venue_list
tester = venue_list['Cattivo']
print(tester().get_response()[0])
for i in tester().get_events():
    print(i.event_output())

# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# db = client.showrunner_db
# collection = db.events

