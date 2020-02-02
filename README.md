## CoinLayerPackage

*****
### The convert_currency's function used to convert amount between one or multiple 

##### Its parameters are:

1. api : `access_key` is a unique identifier that identify the calling application or user.
2. Symbol1 : is the code of the currency to convert from.
3. Symbol2 : is the code of the currency to convert to.
4. amount : is the amount to be converted.
*****

*****
### The fetch_historical_data's function used to query the API for historical crypto data

##### Its parameters are:

1. api : (access_key) is a unique identifier that identify the calling application or user..
2. symbol: is one or multiple cryptocurrency symbols "separated with comma"
3. target: is a target currency
. date : is a date in `YYYY-MM-DD` format.
*****

*****
### The fetch_time_frame's function used to query the API for time-series crypto data between two dates.

##### Its parameters are:

api : `access_key` is a unique identifier that identify the calling application or user.
start_date : is a start date for a time frame in `YYYY-MM-DD`format.
end-date : is a an end date for a time frame in `YYYY-MM-DD` format.
symbol: is one or multiple cryptocurrency symbols "separated with comma"
target: is a target currency.
*****
