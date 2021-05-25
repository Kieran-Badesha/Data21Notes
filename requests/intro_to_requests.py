import json
import requests
from pprint import pprint

# Single postcode request
# post_code_req = requests.get("https://api.postcodes.io/postcodes/B140EG")
#
# print(post_code_req.json())


# Multiple postcode request
json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes",
                               headers=headers, data=json_body)

pprint(post_multi_req.json()['result'][2]['result']['ced'])
pprint(post_multi_req.json()['result'][0]['result']['ced'])
