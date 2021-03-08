# MODULES

import requests

target = input('[+] Target: ')

req = requests.get(f'http://ip-api.com/json/{target}')
res = req.json()
print(f'''
    IP : {res['query']}
    Status : {res['status']}
    Country: {res['country']}
    C Code : {res['countryCode']}
    Region : {res['region']}
    RegionName: {res['regionName']}
    City   : {res['city']}
    Zip    : {res['zip']}
    Latitute : {res['lat']}
    Lontitute : {res['lon']}
    TimeZone : {res['timezone']}
    Isp : {res['isp']}
    Org : {res['org']}
    as : {res['as']}

''')
# KEMBANGIN
