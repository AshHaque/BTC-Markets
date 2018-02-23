import requests
from config import domain
from helper import build_headers

# Global Vars
uri = "/account/balance"
url = domain + uri


def main():

    res = build_headers(uri)
    print(res)
    r = requests.get(url, headers=res, verify=True)

    audbal = r.json()[0]
    btcbal = r.json()[1]
    ltcbal = r.json()[2]

    print(r.json()[3])
    print(r.json()[4])
    print(r.json()[5])
    print(r.json()[6])
    print(audbal)
    print(btcbal)
    print(ltcbal)
    print(r.headers)
    print(r.headers)


if __name__ == "__main__":
    main()