from venue_classes.all_venues import venue_list
from db_maintenence.check_dups import check_existing
tester = venue_list['Steamworks']
print(tester().get_events())
for i in tester().get_events():
    print(i.event_date)
#     if check_existing(i.event_output()['event_id']) > 0:
#         print('skipped')
#         next
