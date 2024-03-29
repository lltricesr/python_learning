"""
    CLI application to perform this retrieval of the bitcoin price
    import the request module
    import the click module -> click has to be installed; pip3 install click
        Command Line Interface Creation Kit (CLICK)
    
    USING COMMAND GROUP
        The CLI to run the application has change now that the click:group is being used.
            The app must include the click:command as a part of the CLI arguments
                NOTE: 'func_name' in code converts to 'func-name' in CLI 
        E.g., 
            (no command group) -> python3 app.py [--coin_id=value --currency=value]
                ex: python3 main.py --coin_id=ethereum --currency=gbp
            (with command group) -> python3 app.py click:command-func-name [--coin_id=value --currency=value]
                ex: python3 main.py show-coin-price --coin_id=ethereum --currency=gbp

    import sqlite3 to perform database operations
    import datetime to add date of investment

    Database
        sell -> 0 = buy, 1 = sell
        date -> stored as a str

    CLI -> ipython to run the db command; ctrl-d to close

    import csv for uploading investments via file

    Row Factories
        Generic collection such as a list of tuples can be confusing to work with, particularly in a larger application.
        using python structured objects
            the row_factory attribute
            sqlite3 includes the Row row factory
            Transform a tuple into a dictionary like object
            use a namedtuple from the collections module
        
"""
import sqlite3
import requests
import click
import datetime
import csv

"""
    Row Factory alternative -> Dataclasses
    #Helper classes / data transfer object
    class Investment:
        def __init__(self, coin_id, currency, amount, sell, date):
            self.coin_id = coin_id
            self.currency = currency
            self.amount = amount
            self.sell = sell
            self.date = date
        def __repr__(self):
            return f"<Investment {self.coin_id} {self.amount:.2f} {self.currency.upper()}>"

    #Dataclass
    from dataclasses import dataclass
    from date import datetime

    @dataclass
    class Investment:
        coin_id: str
        currency: str
        amount: float
        sell: bool
        date: datetime.datetime

    def compute_value(self) -> float:
        return self.amount * get_coin_price(self.coin_id, self.currency)

    #Row Factory (function)
    
    #Inputs
        # _ -> a cursor; but since it is not used in the function
        # row -> a tuple representing the row
        # return -> instantiated Investment storing all the elements of the tuple in the attributes of the class
        # sell -> stored in db as an int 0/1; converted to False/True using the cast of bool()
        # date -> stored in db as an str; coverted to datetime using the datetime:strptime method
    def investment_row_factory(_, row):
        return Investment(
            coin_id = row[0],
            currency = row[1],
            amount = row[2],
            sell = bool(row[3]),
            date = datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S.%f")
        )

    #Now set the row factory to the database obj
    #database:row_factory -> initializes what row factory func will be used to produce the instantiated obj as row
    #now the results of sql queries will be investment obj
    database.row_factory = investment_row_factory

    #accessing results
        #instead of -> row[2] {aka amount} = 10.0
        #replaced by -> row.amount = 10.0
"""

CREATE_INVESTMENTS_SQL = """
    CREATE TABLE IF NOT EXISTS investments (
        coin_id TEXT,
        currency TEXT,
        amount REAL,
        sell INT,
        date TIMESTAMP
    );
"""

"""
    coin_id -> the id for the cryptocurrency to look up; e.g., bitcoin, ethereum, tether, bnb, solana, xrp, usdc, cardano
    currency -> which currency to get the value of price in; e.g., usd, gpp, euro, cad, chf, ils, inr, mxn, cop
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
    return coin_price

"""
    @click.group() -> when executing more than 1 command
    this allows you to group commands together using the (func_name)cli.add_command(click:command) 
"""
@click.group()
def cli():
    pass

"""
    @click.command() -> to mark for CLI enabled
    @click.option("opt", default="val") -> parse the options from the CLI; adding the default makes the option optional
    coin_id -> the id for the cryptocurrency to look up; e.g., bitcoin, ethereum, tether, bnb, solana, xrp, usdc, cardano
    currency -> which currency to get the value of price in; e.g., usd, gpp, euro, cad, chf, ils, inr, mxn, cop
    get_coin_price -> func to call url and retrive coin_price
"""
@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def show_coin_price(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    print(f"The price of {coin_id} is {coin_price:.2f} {currency.upper()}")

"""
    Click command to add an investment
    coin_id -> the id for the cryptocurrency to buy/sell; e.g., bitcoin, ethereum, tether, bnb, solana, xrp, usdc, cardano
    currency -> which currency to get the value of price in; e.g., usd, gpp, euro, cad, chf, ils, inr, mxn, cop
    amount(float) -> cost/price of investment in given currency
    sell(bool:int) -> Buy=False/Sell=True; default=True
    sql -> paramterize query for adding a new investment
    values(tuple) -> all the options plus an explicit defined datetime
    cursor:execute -> execute the sql with values
    database:commit -> commit changes to the database
    print message to user
"""
@click.command
@click.option("--coin_id")
@click.option("--currency")
@click.option("--amount", type=float)
@click.option("--sell", is_flag=True)
def add_investment(coin_id, currency, amount, sell):
    sql = "INSERT INTO investments VALUES (?, ?, ?, ?, ?);"
    values = (coin_id, currency, amount, sell, datetime.datetime.now())
    cursor.execute(sql, values)
    database.commit()

    if sell:
        print(f"Added sell of {amount} {coin_id}")
    else:
        print(f"Added buy of {amount} {coin_id}")

"""
    select investments for buy or sell
    get current value of investments
    coin_id -> the type of crytocurrency to invest
    currency -> the trading currency of the investment
    get_coin_price -> return current price value of crytocurrency from Coin Gecko
    sql -> parameterized select query based on sell or buy
    buy_result -> result set for all buy investments
    sell_result -> result set for all sell investments
    buy_amount -> sum of all buy_results amounts
    sell_amount -> sum of all sell_results amounts
    total -> difference of buy & sell amount of investment value for cryto in currency
"""
@click.command()
@click.option("--coin_id")
@click.option("--currency")
def get_investment_value(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    sql = """
        SELECT amount
        FROM investments
        WHERE coin_id=?
        AND currency=?
        AND sell=?;
    """
    buy_result = cursor.execute(sql, (coin_id, currency, False)).fetchall()
    sell_result = cursor.execute(sql, (coin_id, currency, True)).fetchall()
    buy_amount = sum([row[0] for row in buy_result])
    sell_amount = sum([row[0] for row in sell_result])

    total = buy_amount - sell_amount

    print(f"You own a total of {total} {coin_id} worth {total * coin_price} {currency.upper()}")

"""
    retrieve investments from cvs file
    csv_file -> comma delimited file with listed investments to make
    open(fn, 'r') -> open in read-only mode
    csv:reader -> method used to read csv and return data rows as a reader
    list(reader) -> convert reader into a list
    sql -> parameterized insert
    cursor:executemany() -> executes many rows at once; replace loop of 1 row at a time
"""
@click.command()
@click.option("--csv_file")
def import_investments(csv_file):
    with open(csv_file, 'r') as current_file:
        reader = csv.reader(current_file, delimiter=",")
        rows = list(reader)
        sql = "INSERT INTO investments VALUES (?, ?, ?, ?, ?);"
        cursor.executemany(sql, rows)
        database.commit()

        print(f"Imported {len(rows)} investments from {csv_file}")

"""
    cli:add_command -> method adding a click:command to a click:group 
"""
cli.add_command(show_coin_price)
cli.add_command(add_investment)
cli.add_command(get_investment_value)
cli.add_command(import_investments)

"""
    special dunder method: __main__ called at the execution/initialization of the module
        this special function is executed behind the scene in all modules
    special dunder method: __name__ can be used to "intercept" the call to __main__ to provide additional checking
        good to use for stoping the auto execution of __main__ when imported into other modules
    
    Calling the click:group -> (func_name)cli to start the program 

    Handle all database setup
        create/connect to database
        create cursor
        create table using SQL
"""
if __name__ == "__main__":
    database = sqlite3.connect("portfolio.db")
    cursor = database.cursor()
    cursor.execute(CREATE_INVESTMENTS_SQL)
    cli()