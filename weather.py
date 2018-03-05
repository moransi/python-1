import requests

## /c/Users/mcse/AppData/Local/Programs/Python/Python36-32/Scripts/pip
## http://maps.googleapis.com/maps/api/geocode/json?address=haifa

resp = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address=haifa')

if resp.status_code != 200:
    # This means something went wrong.
    raise requests.RequestException('GET ERROR {}'.format(resp.status_code))

j_resp = resp.json()
print(j_resp)

## results ---> list item #0 ---> geometry ---> location

results = j_resp['results'][0]
location = results['geometry']['location']
lat = location['lat']
lng = location['lng']

#darksky_url = f"https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/{lat},{lng}"

resp = requests.get('https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/32.7996897,34.9817565')
# if resp.status_code != 200:
#     # This means something went wrong.
#     raise requests.RequestException('GET ERROR {}'.format(resp.status_code))
#
# j_resp = resp.json()

# print(resp.json())

