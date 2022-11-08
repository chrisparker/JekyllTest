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

print("theta.json written. Creating allrep folder")

os.mkdir("docs/_allrep")

print("allrep folder created. Writing allreps")

for simpleGroup in theta["caboodle"]:
  with open('docs/_allrep/' + simpleGroup["name"] + '.md', 'w') as f:
    f.write("---\r\n")
    f.write("data: " + json.dumps(simpleGroup) + '\r\n')
    f.write("layout: allrep\r\n")
    f.write("---\r\n")    

print("allreps written. Creating permreps folder")

os.mkdir("docs/_permrep")

print("permrep folder created. Writing permreps")

for simpleGroup in theta["caboodle"]:
  groupName = simpleGroup["name"]
  batch = simpleGroup["batch"]
  for isoGroup in simpleGroup.get("isoGroups", []):
    for permRep in isoGroup.get("permReps", []):
      for basis in permRep.get("bases", []):
        with open('docs/_permrep/' + permRep["name"] + basis["name"] +'.md', 'w') as f:
          f.write("---\r\n")
          f.write("permRep: " + json.dumps(permRep) + '\r\n')
          f.write("basis: " + json.dumps(basis) + '\r\n')
          f.write("simpleGroup: " + json.dumps(simpleGroup) + '\r\n')
          f.write("layout: permrep\r\n")
          f.write("---\r\n")    
        
print("permrep written. Creating matrep folder")

os.mkdir("docs/_matrep")

print("matrep folder created. Writing char0reps to matrep folder")

for simpleGroup in theta["caboodle"]:
  groupName = simpleGroup["name"]
  batch = simpleGroup["batch"]
  for isoGroup in simpleGroup.get("isoGroups", []):
    for char0Rep in isoGroup.get("char0Reps", []):
      for basis in char0Rep.get("bases", []):
        with open('docs/_matrep/' + char0Rep["name"] + basis["name"] +'.md', 'w') as f:
          f.write("---\r\n")
          f.write("rep: " + json.dumps(char0Rep) + '\r\n')
          f.write("basis: " + json.dumps(basis) + '\r\n')
          f.write("simpleGroup: " + json.dumps(simpleGroup) + '\r\n')
          f.write("layout: matrep\r\n")
          f.write("---\r\n")    
       
print("char0reps written. Writing modular reps to matrep folder")

for simpleGroup in theta["caboodle"]:
  groupName = simpleGroup["name"]
  batch = simpleGroup["batch"]
  for isoGroup in simpleGroup.get("isoGroups", []):
    for modularRep in isoGroup.get("modularReps", []):
      for basis in modularRep.get("bases", []):
        with open('docs/_matrep/' + modularRep["name"] + basis["name"] +'.md', 'w') as f:
          f.write("---\r\n")
          f.write("rep: " + json.dumps(modularRep) + '\r\n')
          f.write("basis: " + json.dumps(basis) + '\r\n')
          f.write("simpleGroup: " + json.dumps(simpleGroup) + '\r\n')
          f.write("layout: matrep\r\n")
          f.write("---\r\n")    
               
print("modular reps written.")
