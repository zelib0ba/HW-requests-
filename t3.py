import requests, datetime
from datetime import datetime

today = datetime.timestamp(datetime.now())

def get_questions(days, tag):
    end_date = int(today)
    start_date = end_date - days * 86400 
    PARAMS = {
        'fromdate' : start_date,
        'todate' : end_date,
        'tagged' : tag,
        'site' : 'stackoverflow'
    }
    
    resp = requests.get('https://api.stackexchange.com/2.2/questions', params = PARAMS)

    for key, question in enumerate(resp.json().get('items')):
        print(f"{key}.{question['title']}")
        
get_questions(2, 'python')
