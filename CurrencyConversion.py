import requests    

def currency_conversion(api,symbol1,symbol2,amount):
    
    url = 'http://api.coinlayer.com/convert?access_key =api &from = symbol1 &to = symbol2 &amount = amount'
    params = {'access_key': api, 'from': symbol1,'to':symbol2, 'amount': amount}
    r = requests.get(url, params = params)
    convcoin = r.json()
    print (convcoin)
    return convcoin
