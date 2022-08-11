from venue_classes.all_venues import venue_list
tester = venue_list['StageAE']
# print(tester().get_response())
for i in tester().get_events():
    print(i.event_output())



