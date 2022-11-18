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

print("Parsed theta.json successfully. Applying sorts to theta.")

for simpleGroup in theta["caboodle"]:
  for isoGroup in simpleGroup.get("isoGroups", []):
    permReps = isoGroup.get("permReps", [])
    permReps.sort(key=lambda x: int(x["points"]))
    char0Reps = isoGroup.get("char0Reps", [])    
    char0Reps.sort(key=lambda x: int(x["dimension"]))
    modularReps = isoGroup.get("modularReps", [])    
    modularReps.sort(key=lambda x: ((1000000*int(x["characteristic"])) + (1000*int(x["field"])) + (int(x["dimension"]))))
    
    
print("Sorts applied successfully. Creating _data folder")

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
        
print("permrep written. Creating char0rep folder")

os.mkdir("docs/_char0rep")

print("char0rep folder created. Writing char0reps to char0rep folder")

for simpleGroup in theta["caboodle"]:
  groupName = simpleGroup["name"]
  batch = simpleGroup["batch"]
  for isoGroup in simpleGroup.get("isoGroups", []):
    for char0Rep in isoGroup.get("char0Reps", []):
      for basis in char0Rep.get("bases", []):
        with open('docs/_char0rep/' + char0Rep["name"] + basis["name"] +'.md', 'w') as f:
          f.write("---\r\n")
          f.write("char0rep: " + json.dumps(char0Rep) + '\r\n')
          f.write("basis: " + json.dumps(basis) + '\r\n')
          f.write("simpleGroup: " + json.dumps(simpleGroup) + '\r\n')
          f.write("layout: char0rep\r\n")
          f.write("---\r\n")    
       
print("char0reps written. Creating modularrep folder")

os.mkdir("docs/_modularrep")

print("modularrep folder created. Writing modularreps to modularrep folder")

for simpleGroup in theta["caboodle"]:
  groupName = simpleGroup["name"]
  batch = simpleGroup["batch"]
  for isoGroup in simpleGroup.get("isoGroups", []):
    for modularRep in isoGroup.get("modularReps", []):
      for basis in modularRep.get("bases", []):
        with open('docs/_modularrep/' + modularRep["name"] + basis["name"] +'.md', 'w') as f:
          f.write("---\r\n")
          f.write("modularrep: " + json.dumps(modularRep) + '\r\n')
          f.write("basis: " + json.dumps(basis) + '\r\n')
          f.write("simpleGroup: " + json.dumps(simpleGroup) + '\r\n')
          f.write("layout: modularrep\r\n")
          f.write("---\r\n")    
               
print("modular reps written.")
