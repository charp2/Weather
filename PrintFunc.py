def printData(i):
    print(i['EnglishName'] + ', ' + i['Country']['EnglishName'])
    print(i['GeoPosition']['Elevation']['Metric']['Value'], end=' ')
    print('m')
    print(i['Temperature']['Metric']['Value'], end=' ')
    print('\xb0C',end='  (')
    print(i['Temperature']['Imperial']['Value'], end=' ')
    print('\xb0F)')
    print('\n')
    return
