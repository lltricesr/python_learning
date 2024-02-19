#import the request module to work with http request
import requests

#variables that represent dynamic data for building url
coin_id = "bitcoin"
currency = "usd"

#coin gecko url
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"

"""
    request -> module to handle http request; reduce boiler plate
    get(url) -> get request to the url
    .json() -> because the content-type in the response is application/json; used to parse response into a json dict
"""
data = requests.get(url).json()

#using the keys in the dict to extract the coin price
coin_price = data[coin_id][currency]

print(coin_price)