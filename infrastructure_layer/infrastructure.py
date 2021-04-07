import json
import requests

headers = {'content-type' : 'application/json'}


def put(URL, data=None):
    return Request(URL, rType='PUT', data=data)


def get(URL, data=None):
    return Request(URL, rType='GET', data=data)


def post(URL, data=None):
    return Request(URL, rType='POST', data=data)


def delete(URL, data=None):
    return Request(URL, rType='DELETE', data=data)


def Request(URL, rType='GET', data=None):
    if data==None:
        r = requests.request(rType, url=URL, headers=headers)
    else:
        if rType == 'GET':
            r = requests.request(rType, url=URL, params=data, headers=headers)
        else:
            r = requests.request(rType, url=URL, data=json.dumps(data), headers=headers)

    return r

