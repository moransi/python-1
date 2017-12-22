import requests

## /c/Users/mcse/AppData/Local/Programs/Python/Python36-32/Scripts/pip


resp = requests.get('https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/32.7996897,34.9817565')
if resp.status_code != 200:
    # This means something went wrong.
    raise requests.RequestException('GET ERROR {}'.format(resp.status_code))

j_resp = resp.json()

print(resp.json())

