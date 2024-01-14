import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'
# the python format for csv's would be the dictionary
# it is really similar to a .json file
# DictReader() is the function to read this kind of file
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r") as f: # "r" is the read mode
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate) # pretty print ^_^
        break
