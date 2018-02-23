import time
import hashlib
import hmac
import base64

from collections import OrderedDict
from config import apikey_secret
from config import apikey_public


askey = apikey_secret.encode("utf-8")
pkey = apikey_public.encode("utf-8")
skey = base64.standard_b64decode(askey)


def build_headers(uri, rbody=None):

    # Build timestamp
    tstamp = time.time()
    ctstamp = int(tstamp * 1000)
    sctstamp = str(ctstamp)

    # Build and sign to construct body
    if rbody is None:
        sbody = uri + "\n" + sctstamp + "\n"
    else:
        sbody = uri + "\n" + rbody + "\n" + sctstamp + "\n"
    # print(sbody)
    rbody = sbody.encode("utf-8")
    rsig = hmac.new(skey, rbody, hashlib.sha512)
    bsig = base64.standard_b64encode(rsig.digest()).decode("utf-8")

    # Construct header list of key value pairs
    headers = OrderedDict()
    headers['Accept'] = "application/json"
    headers['Accept-Charset'] = "UTF-8"
    headers['Content-Type'] = "application/json"
    headers['apikey'] = pkey
    headers['timestamp'] = sctstamp
    headers['signature'] = bsig
    headers = dict(headers)
    # print(headers)

    return headers