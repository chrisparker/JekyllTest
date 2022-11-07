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

print("theta.json written. Creating allreps folder")

os.mkdir("docs/_data/allreps")

print("allreps folder created. Writing allreps")

for simpleGroup in theta["caboodle"]:
  with open('docs/_data/allreps/' + simpleGroup["name"] + '.json', 'w') as f:
    json.dump(simpleGroup, f)      

print("allreps written. Creating permreps folder")

os.mkdir("docs/_data/permreps")

print("permreps folder created. Writing permreps")

for simpleGroup in theta["caboodle"]:
  groupName = simpleGroup["name"]
  batch = simpleGroup["batch"]
  for isoGroup in simpleGroup.get("isoGroups", []):
    for permRep in isoGroup.get("permReps", []):
      with open('docs/_data/permreps/' + permRep["name"] + '.json', 'w') as f:
        json.dump(permRep, f)
        
print("permreps written")