import requests
import json
from config import domain
from helper import build_headers
from collections import OrderedDict

# Global Vars
uri = "/order/history"
url = domain + uri


def main():

    reqbody = OrderedDict()
    reqbody['currency'] = "AUD"
    reqbody['instrument'] = "BTC"
    reqbody['limit'] = 10
    reqbody['since'] = 0
    # print(reqbody)
    reqbody = json.dumps(reqbody)
    # print(reqbody)

    res = build_headers(uri, reqbody)
    # print(res)
    # r = requests.post(url, headers=res, verify=True)
    payload = {}
    r = requests.post(url, data=json.dumps(payload), headers=res, verify=True)

    # audbal = r.json()[0]
    # print(r.headers)
    # print(r.url)

    print(r)



if __name__ == "__main__":
    main()