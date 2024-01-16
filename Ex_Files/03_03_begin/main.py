import csv # read csv
import json # read json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
} # this is not a json but a Python dictionary

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json) # convert back to dictionary
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as f: # r = read mode; as file object
    reader = csv.DictReader(f)
    laureates = list(reader)


with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
