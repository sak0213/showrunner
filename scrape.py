import pymongo
from venue_classes.all_venues import venue_list
from db_maintenence.check_dups import check_existing

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.showrunner_db
collection = db.events

duplicate_counter = 0
addition_counter = 0

# FULL RUN OF LIST
for venue in venue_list.values():
    for event in venue().get_events():
        if check_existing(event.event_output()['event_id']) > 0:
            duplicate_counter += 1
            next
        else:
            collection.insert_one(event.event_output())
            addition_counter += 1
print(f'Update Complete! Added {addition_counter} new events and skipped {duplicate_counter} duplicates.')
