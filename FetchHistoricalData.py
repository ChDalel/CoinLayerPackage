import requests

def fetch_historical_data(api,symbol,target,date):
    url = 'http://api.coinlayer.com/date? access_key =api &symbols = symbol &target=target,YYYY-MM-DD=date'
    params = {'access_key': api,'symbols': symbol,'target': target,'YYYY-MM-DD' : date}
    r = requests.get(url, params = params)
    convcoin = r.json()
    print (convcoin)
    return convcoin
