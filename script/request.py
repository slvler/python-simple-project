import json
import requests


def swapi_status_code():
    site = requests.get('https://swapi.dev/api/people/1')
    print(site.status_code)

def swapi_headers():
    site = requests.get("https://swapi.dev/api/people/1")
    print(site.headers)

def swapi_response():
    site = requests.get("https://swapi.dev/api/people/1")
    print(site.json())
    v = site.json()
    print(v['name'])
    for i in site.json():
        print(i)
    #print(site.content)



def postman_post():
    values = requests.post("https://48b6e4c4-8839-4d68-bee7-efad9638459b.mock.pstmn.io/callback/setting/post")
    print(values.json())
def postman_post_parametre():
    url = "https://48b6e4c4-8839-4d68-bee7-efad9638459b.mock.pstmn.io/callback/setting/request"
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(url, data=payload)
    print(r.json())

def postman_header():
    url = "https://48b6e4c4-8839-4d68-bee7-efad9638459b.mock.pstmn.io/callback/setting/request"
    payload = { 'some': 'data' }
    headers = { 'content-type': 'application/json' }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.json())


def postman_params():

    url = "https://48b6e4c4-8839-4d68-bee7-efad9638459b.mock.pstmn.io"
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get(url, params=payload)



postman_post_parametre()
#postman_post()
#swapi_headers()
#swapi_response()
#swapi_status_code()