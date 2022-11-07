#!/usr/bin/env python3
  
import json
import os

class Group:
  def __init__(self, batch, groupName, permRepName):
    self.batch = batch
    self.groupName = groupName
    self.permRepName = permRepName

print("Reading theta.json")

f = open("brook/theta.json", "r")
fileContent = f.read()
f.close()

print("theta.json read. Parsing as json")

theta = json.loads(fileContent)

print("Parsed theta.json successfully. Creating _data folder")

os.mkdir("docs/_data")

print("Created _data folder. Writing theta.json to output.")

with open('docs/_data/theta.json', 'w') as f:
    json.dump(theta, f)

