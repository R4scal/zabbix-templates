#!/usr/bin/env python

import os
import json
import requests
from os.path import dirname
import nicehash_settings

def getProf():
        url = 'https://api.nicehash.com/api'

        params = dict(
            method='stats.provider.ex',
            addr= nicehash_settings.btcAddress
        )

        resp = requests.get(url=url, params=params)
        stats = json.loads(resp.text)

        totalProf = 0
        for i in stats["result"]["current"]:
            algoProf = float(i["profitability"])
            if "a" in i["data"][0]:
                totalProf = totalProf + algoProf * float(i["data"][0]["a"])
        return totalProf

prof = getProf()
print prof
