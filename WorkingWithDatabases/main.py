"""
    CLI application to perform this retrieval of the bitcoin price
    import the request module
    import the click module -> click has to be installed; pip3 install click
        Command Line Interface Creation Kit (CLICK)
"""
import requests
import click

"""
    coin_id -> the id for the cryptocurrency to look up; e.g., bitcoin, ethereum, tether, bnb, solana, xrp, usdc, cardano
    currency -> which currency to get the value of price in; e.g., usd, euro, cad, chf, ils, inr, mxn, cop
    url -> the url equivalency as based by Coin Gecko
    request -> module to handle http request; reduce boiler plate
    get(url) -> get request to the url
    .json() -> because the content-type in the response is application/json; used to parse response into a json dict
    data -> parsed dictionary from the json
"""
def get_coin_price(coin_id,currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]
    print(f"The price of {coin_id} is {coin_price:.2f} {currency.upper()}")