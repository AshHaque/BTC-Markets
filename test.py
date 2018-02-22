
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


def build_headers(URL, PUBKEY, PRIVKEY):

    # Build timestamp
    tstamp = time.time()
    ctstamp = int(tstamp * 1000)
    sctstamp = str(ctstamp)

    # Build and sign to construct body

    reqbody = OrderedDict([("currency", "AUD"),
                           ("instrument", "BTC"),
                           ("limit", "10"),
                           ("since", "1018208972")])

    reqbodydic = json.dumps(dict(reqbody))


    sbody = uri + "\n" + reqbodydic + "\n" + sctstamp + "\n"
    print(sbody)
    rbody = sbody.encode("utf-8")
    rsig = hmac.new(skey, rbody, hashlib.sha512)
    bsig = base64.standard_b64encode(rsig.digest()).decode("utf-8")

    # Construct header list of key value pairs
    headers_list = OrderedDict([("Accept", "application/json"),
                                ("Accept-Charset", "UTF-8"),
                                ("Content-Type", "application/json"),
                                ("apikey", pkey),
                                ("timestamp", "1519275095335"),
                                ("signature", bsig)])
    # Load list into dictionary
    headers = dict(headers_list)

    return headers

uri = "/order/trade/history"
url = domain + uri
askey = apikey_secret.encode("utf-8")
pkey = apikey_public.encode("utf-8")
skey = base64.standard_b64decode(askey)

header = build_headers(url, pkey, skey)
reqbody = OrderedDict([])

reqbodydic = json.dumps(dict(reqbody))
data = reqbodydic.encode("utf-8")
print("Header:",header)
print("Payload:",data)

req = urllib.request.Request(url, data, header)
response = urllib.request.urlopen(req)
print("\nResponse:",response.read())