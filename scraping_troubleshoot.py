from venue_classes.all_venues import venue_list
from db_maintenence.check_dups import check_existing
tester = venue_list['StageAE']
# print(tester().get_response())
for i in tester().get_events():
    if check_existing(i.event_output()['event_id']) > 0:
        print('skipped')
        next
