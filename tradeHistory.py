import requests
import time
import hashlib
import hmac
import base64
import json
import urllib.request



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

    # Build and sign to construct body


    sbody = uri + "\n" + sctstamp + "\n"
    print(sbody)
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

    reqheader = build_headers(url, pkey, skey)
    reqbody = [("currency", "AUD"),
                                ("instrument", "BTC"),
                                ("limit", "10"),
                                ("since", "0")]

    reqbodydic = json.dumps(dict(reqbody))

    # r = requests.post(url, headers=res, verify=True)
    # r = requests.post(url, data=res)

    req = urllib.request.Request(url)
    req.add_header(reqheader)
    print(req)
    r = urllib.urlopen(req, reqbodydic)
    print(r)

    result = r.json()

    print(result)


if __name__ == "__main__":
    main()