import json
import requests

# Single postcode request
# post_code_req = requests.get("https://api.postcodes.io/postcodes/B140EG")
#
# print(post_code_req.json())


# Multiple postcode request
json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())
