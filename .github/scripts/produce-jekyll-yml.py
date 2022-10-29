#!/usr/bin/env python3
  
import json

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

print("Parsed theta.json successfully. Generating groups.yml")

groups = []

for simpleGroup in theta["caboodle"]:
  groupName = simpleGroup["name"]
  batch = simpleGroup["batch"]
  for isoGroup in simpleGroup.get("isoGroups", []):
    for permRep in isoGroup.get("permReps", []):
      permRepName = permRep["name"]
      newGroup = Group(batch, groupName, permRepName)  
      groups.append(newGroup)

f = open("docs/_data/groups.yml", "w")
for group in groups:
  f.write("- groupName: ")
  f.write(group.groupName)
  f.write("\n")
  
  f.write("  batch: ")
  f.write(group.batch)
  f.write("\n")
  
  f.write("  permRepName: ")
  f.write(group.permRepName)
  f.write("\n")
    
f.close()

print("Generated groups.yml successfully")