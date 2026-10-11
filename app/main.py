import json
from decimal import Decimal


def calculate_profit(filename: str):
    with open(filename, "r") as f:
        trades_data = json.load(f)
        for trade_session in trades_data:
            sold_money = 0
            bought_money = 0
            price = Decimal(trade_session["matecoin_price"])
            if trade_session["bought"]:
                bought = Decimal(trade_session["bought"]) 
                bought_money = bought * price
            else:
                sold = Decimal(trade_session["sold"])
                sold_money = sold * price
            