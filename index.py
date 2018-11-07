#!/usr/bin/python

import requests
import json

from Utilities import printData
from Utilities import shiftList

queryParams = [('apikey', 'PWNs0VAtZYOJUqDR1FTpXY5DG5r2CRJ0'), ('details', 'true')]

resp = requests.request(
method='GET',
url='http://dataservice.accuweather.com/currentconditions/v1/topcities/150',
headers=None, files=None, data=None, params=queryParams, auth=None,
cookies=None, hooks=None, json=None)

r = json.loads(resp.text)

maxTempCities = r[0:5]
minTempCities = r[0:5]

for i in r:
    temp = i['Temperature']['Metric']['Value']

    for j in range(0, len(maxTempCities)):
        maxTemp = maxTempCities[j]['Temperature']['Metric']['Value']
        if temp > maxTemp:
            maxTempCities = shiftList(j, maxTempCities)
            maxTempCities[j] = i
            break

    for j in range(0, len(minTempCities)):
        minTemp = minTempCities[j]['Temperature']['Metric']['Value']
        if temp < minTemp:
            minTempCities = shiftList(j, minTempCities)
            minTempCities[j] = i
            break

print('Hottest:')
for maxTempCity in maxTempCities:
    printData(maxTempCity)

print('Coldest:')
for minTempCity in minTempCities:
    printData(minTempCity)
