# -*- coding: utf-8 -*-
"""retrieve the tradable instruments for account."""

import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.transactions as transactions
import oandapyV20.endpoints.pricing as pricing
from exampleauth import exampleAuth


# account
def print_instruments(api: oandapyV20.API, acc: str):
    r = accounts.AccountInstruments(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_summary(api: oandapyV20.API, acc: str):
    r = accounts.AccountSummary(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_details(api: oandapyV20.API, acc: str):
    r = accounts.AccountDetails(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_accounts(api: oandapyV20.API):
    r = accounts.AccountList()
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# instrument
def print_candles(api: oandapyV20.API):
    param = {
        'count': 6
    }
    r = instruments.InstrumentsCandles('XAU_USD', params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_orderbook(api: oandapyV20.API):
    r = instruments.InstrumentsOrderBook('XAU_USD')
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_positionbook(api: oandapyV20.API):
    r = instruments.InstrumentsPositionBook('XAU_USD')
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# order
def print_orders(api: oandapyV20.API, acc: str):
    r = orders.OrderList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_pending_orders(api: oandapyV20.API, acc: str):
    r = orders.OrdersPending(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# trade
def print_trades(api: oandapyV20.API, acc: str):
    r = trades.TradesList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_opentrades(api: oandapyV20.API, acc: str):
    r = trades.OpenTrades(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# positions
def print_positions(api: oandapyV20.API, acc: str):
    r = positions.PositionList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_open_positions(api: oandapyV20.API, acc: str):
    r = positions.OpenPositions(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# transactions
def print_transactions(api: oandapyV20.API, acc: str):
    r = transactions.TransactionList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# pricing
def print_pricing(api: oandapyV20.API, acc: str):
    param = {
        'instruments': 'XAU_USD'
    }
    r = pricing.PricingInfo(accountID=acc, params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def main():
    accountID, token = exampleAuth()
    client = oandapyV20.API(access_token=token)

    # account
    # print_instruments(client, accountID)
    # print_summary(client, accountID)
    # print_details(client, accountID)
    # print_accounts(client)

    # instrument
    # print_candles(client)
    # print_orderbook(client)
    # print_positionbook(client)

    # order
    # print_orders(client, accountID)
    # print_pending_orders(client, accountID)

    # trade
    # print_trades(client, accountID)
    # print_opentrades(client, accountID)

    # position
    # print_positions(client, accountID)
    # print_open_positions(client, accountID)

    # transaction
    # print_transactions(client, accountID)

    # pricing
    print_pricing(client, accountID)


if __name__ == '__main__':
    main()
