#!/usr/bin/python

import requests
import json

from PrintFunc import printData

queryParams = [('apikey', 'PWNs0VAtZYOJUqDR1FTpXY5DG5r2CRJ0'), ('details', 'true')]

resp = requests.request(
method='GET',
url='http://dataservice.accuweather.com/currentconditions/v1/topcities/150',
headers=None, files=None, data=None, params=queryParams, auth=None,
cookies=None, hooks=None, json=None)

r = json.loads(resp.text)

for i in r:
    printData(i)

maxTempCity = r[0]
minTempCity = r[0]
for i in r:
    temp = i['Temperature']['Metric']['Value']
    maxTemp = maxTempCity['Temperature']['Metric']['Value']
    minTemp = minTempCity['Temperature']['Metric']['Value']
    if temp > maxTemp:
        maxTempCity = i
    elif temp < minTemp:
        minTempCity = i

print('Hottest:')
printData(maxTempCity)

print('Coldest:')
printData(minTempCity)
