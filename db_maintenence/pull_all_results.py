from pymongo import MongoClient
import pandas as pd
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={}

result = client['showrunner_db']['events'].find(
  filter=filter
)

df = pd.DataFrame.from_dict(result)
df['event_date'] = pd.to_datetime(df['event_date'])
df = df[df['event_date'] == '2022-09-25']
print(df.head())
