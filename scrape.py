# # import pymongo
# from venues.mr_smalls import mrsmalls
# from venues.club_cafe import clubcafe
#
# # conn = 'mongodb://localhost:27017'
# # client = pymongo.MongoClient(conn)
# # db = client.showrunner_db
# # collection = db.events
#
# venues = [mrsmalls]
# for venue in venues:
#     for event in venue():
#         print(event)

from venue_classes.all_venues import venue_list
tester = venue_list['Thunderbird']
print(tester().get_response()[0])
for i in tester().get_events():
    print(i.event_output())

