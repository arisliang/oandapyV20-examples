# -*- coding: utf-8 -*-
"""retrieve the tradable instruments for account."""

import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
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
    print_positionbook(client)


if __name__ == '__main__':
    main()
