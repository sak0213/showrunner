from pymongo import MongoClient
from datetime import datetime
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={
    'event_venue': 'Mr. Smalls'
}
project={
    'event_date': 1
}
limit=1

result = client['showrunner_db']['events'].find(
  filter=filter,
  projection=project,
  limit=limit
)
the_date = result[0]['event_date']
print('The original Date')
print(the_date)
new_date = datetime.strptime(the_date,'%A, %B %d, %Y').date()
print(new_date)
