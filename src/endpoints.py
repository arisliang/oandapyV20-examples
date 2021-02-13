# -*- coding: utf-8 -*-
"""retrieve the tradable instruments for account."""

import sys
import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.transactions as transactions
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.forexlabs as labs
from exampleauth import exampleAuth


# account
def print_instruments(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    param = {
        'instruments': 'XAU_USD,EUR_USD'
    }
    r = accounts.AccountInstruments(accountID=acc, params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_summary(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = accounts.AccountSummary(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_details(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = accounts.AccountDetails(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_accounts(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    r = accounts.AccountList()
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# instrument
def print_candles(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    param = {
        'granularity': 'M1',
        'count': 6
    }
    r = instruments.InstrumentsCandles('XAU_USD', params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_orderbook(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    r = instruments.InstrumentsOrderBook('XAU_USD')
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_positionbook(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    r = instruments.InstrumentsPositionBook('XAU_USD')
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# order
def print_orders(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = orders.OrderList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_pending_orders(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = orders.OrdersPending(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# trade
def print_trades(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = trades.TradesList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_opentrades(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = trades.OpenTrades(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# positions
def print_positions(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = positions.PositionList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_open_positions(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = positions.OpenPositions(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# transactions
def print_transactions(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    r = transactions.TransactionList(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# pricing
def print_pricing(api: oandapyV20.API, acc: str):
    print(sys._getframe().f_code.co_name)

    param = {
        'instruments': 'XAU_USD'
    }
    r = pricing.PricingInfo(accountID=acc, params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


# forexlabs
def print_autochartist(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    param = {
        'instrument': 'XAU_USD'
    }
    r = labs.Autochartist(params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_calendar(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    param = {
        'instrument': 'XAU_USD',
        "period": 86400
    }
    r = labs.Calendar(params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_commitments_traders(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    param = {
        'instrument': 'XAU_USD'
    }
    r = labs.CommitmentsOfTraders(params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_historical_position_ratios(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    # The v1 historical_position_ratios endpoint has been disabled.
    # Please use the v20-REST API to derive the position ratio values
    param = {
        'instrument': 'XAU_USD',
        "period": 86400
    }
    r = labs.HistoricalPositionRatios(params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_orderbook_data(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    # The v1 orderbook_data endpoint has been disabled.
    # It has been replaced by the orderBook and positionBook endpoints in the v20-REST API.
    param = {
        'instrument': 'XAU_USD',
        "period": 3600
    }
    r = labs.OrderbookData(params=param)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_spreads(api: oandapyV20.API):
    print(sys._getframe().f_code.co_name)

    param = {
        'instrument': 'XAU_USD',
        "period": 57600
    }
    r = labs.Spreads(params=param)
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
    print_candles(client)
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
    # print_pricing(client, accountID)

    # forexlab
    # print_autochartist(client)
    # print_calendar(client)
    # print_commitments_traders(client)
    # print_historical_position_ratios(client)
    # print_orderbook_data(client)
    # print_spreads(client)


if __name__ == '__main__':
    main()
