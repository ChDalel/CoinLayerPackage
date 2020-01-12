import requests 

def fetch_tima_frame(api,start_date,end_date,symbol,target):
    url = 'http://api.coinlayer.com/date? access_key = 4976d29d2ffb43259ac94f12ff54646d &start_date = start_date &end_date = end_date &symbols = symbol &target=target'
    params = {'access_key': api,'start_date':start_date,'end_date':end_date,'symbols': symbol,'target': target}
    r = requests.get(url, params = params)
    convcoin = r.json()
    print (convcoin)
    return convcoin
