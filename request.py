import requests

def get_request(url):
    res = requests.get(url, verify=False).content
    res = str(res, encoding="utf8").replace("\t", "")
    return res
