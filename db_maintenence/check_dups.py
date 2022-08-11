from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

def check_existing(id):
    filter = {
        'event_id': id
    }
    result = list(client['showrunner_db']['events'].find(
        filter=filter
    ))
    return len(result)
