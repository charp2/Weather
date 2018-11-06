#!/usr/bin/python

import requests
import json

queryParams = [('apikey', 'PWNs0VAtZYOJUqDR1FTpXY5DG5r2CRJ0'), ('details', 'true')]

resp = requests.request(
method='GET',
url='http://dataservice.accuweather.com/currentconditions/v1/topcities/150',
headers=None, files=None, data=None, params=queryParams, auth=None,
cookies=None, hooks=None, json=None)

r = json.loads(resp.text)

for i in r:
    print(i['EnglishName'] + ', ' + i['Country']['EnglishName'])
    print(i['GeoPosition']['Elevation']['Metric']['Value'], end=' ')
    print('m')
    print(i['Temperature']['Metric']['Value'], end=' ')
    print('\xb0C',end='  (')
    print(i['Temperature']['Imperial']['Value'], end=' ')
    print('\xb0F)')
    print('\n')
