# this is purely to understand how to handle different web APIs.
# https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236

import requests
from requests.api import request
import json

testrequest = requests.get("http://api.open-notify.org")
print(testrequest.text)
# prints out the pure html code if the specific target endpoint is not hit

print(f"successful request: {testrequest.status_code}")
# prints out code of 200 if endpoint is hit succesfully, 404 if webpage not found and we hit a failed endpoint

eg_failedrequest = requests.get("http://api.open-notify.org/fake-endpoint")
print(f"failed request: {eg_failedrequest.status_code}")
# this will return an exit code of 404 due to us hitting a failed endpoint

# an example use case

people_in_space = requests.get("http://api.open-notify.org/astros.json")
# here is an example of hitting a succesful end point (URL), which returns specific information in our desired format

print(json.loads(people_in_space.text))
# we can use the json in built python library and the json.loads() method to convert json string to a json file format

for person in json.loads(people_in_space.text)["people"]:
    print(person["name"])
# we are also able to access each indivual element in the json using dictionary methods
