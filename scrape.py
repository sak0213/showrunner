import pymongo
from venue_classes.all_venues import venue_list
# tester = venue_list['Crafthouse']
# # print(tester().get_response())
# for i in tester().get_events():
#     print(i.event_output())

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.showrunner_db
collection = db.events
#
# searcher = collection.find()
# for item in searcher:
#     print(item)



#FULL RUN OF LIST
# for venue in venue_list.values():
#     for event in venue().get_events():
#         collection.insert_one(event.event_output())

