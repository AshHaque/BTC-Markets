import requests
import time
import hashlib
import hmac
import base64
import json

from collections import OrderedDict
from config import apikey_secret
from config import apikey_public
from config import domain

# Define Global Vars
uri = "/order/trade/history"
url = domain + uri
askey = apikey_secret.encode("utf-8")
pkey = apikey_public.encode("utf-8")
skey = base64.standard_b64decode(askey)


def build_headers(URL, PUBKEY, PRIVKEY):

    # Build timestamp
    tstamp = time.time()
    ctstamp = int(tstamp * 1000)  # or int(tstamp * 1000) or round(tstamp * 1000)
    sctstamp = str(ctstamp)

    # Optional timestamping method, not recommended as ticker results may
    # be cached beyond the authentication window.
    #
    # urt = "/market/BTC/AUD/tick"
    # turl = domain + urt
    # rt = requests.get(turl, verify=True)
    # tstamp = r.json()["timestamp"]
    # ctstamp = tstamp * 1000


    # Build and sign to construct body

    reqbody = OrderedDict([("currency", "AUD"),
                                ("instrument", "BTC"),
                                ("limit", "10"),
                                ("since", "1018208972")])

    reqbodydic = json.dumps(dict(reqbody))

    sbody = uri + "\n" + sctstamp + "\n" + reqbodydic + "\n"
    rbody = sbody.encode("utf-8")
    rsig = hmac.new(skey, rbody, hashlib.sha512)
    bsig = base64.standard_b64encode(rsig.digest()).decode("utf-8")

    # Construct header list of key value pairs
    headers_list = OrderedDict([("Accept", "application/json"),
                                ("Accept-Charset", "UTF-8"),
                                ("Content-Type", "application/json"),
                                ("apikey", pkey),
                                ("timestamp", sctstamp),
                                ("signature", bsig)])
    # Load list into dictionary
    headers = dict(headers_list)

    return headers


def main():

    res = build_headers(url, pkey, skey)
    print(res)
    #r = requests.post(url, headers=res, verify=True)
    r = requests.post(url, data=res)
    print(r)

    result = r.json()

    print(result)


if __name__ == "__main__":
    main()