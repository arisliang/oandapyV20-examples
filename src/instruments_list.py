# -*- coding: utf-8 -*-
"""retrieve the tradable instruments for account."""

import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
from exampleauth import exampleAuth


def print_instruments(api: oandapyV20.API, acc: str):
    r = accounts.AccountInstruments(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def print_summary(api: oandapyV20.API, acc: str):
    r = accounts.AccountSummary(accountID=acc)
    rv = api.request(r)
    print(json.dumps(rv, indent=2))


def main():
    accountID, token = exampleAuth()
    client = oandapyV20.API(access_token=token)
    # print_instruments(client, accountID)
    print_summary(client, accountID)


if __name__ == '__main__':
    main()
