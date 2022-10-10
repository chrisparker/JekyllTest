#!/usr/bin/env python3
  
class Group:
  def __init__(self, category, groupName, objectType, objectName, fullPath):
    self.category = category
    self.groupName = groupName
    self.objectType = objectType
    self.objectName = objectName
    self.fullPath = fullPath
        
f = open("find-output.txt", "r")

groups = []

for x in f:
  segments = x.split('/')
  for segment in segments:
    if segment == ".":  
      #Do nothing
      hasRoot = "False"
    elif segment == "spor":
      category = "Sporadic"
    elif segment == "Co1":
      groupName = "Conway 1"
    elif segment == "mtx":
      objectType = "Matrix"
    else:
      objectName = segment
    
  newGroup = Group(category, groupName, objectType, objectName, x)
  
  groups.append(newGroup)

f.close()

f = open("../../docs/_data/groups.yml", "w")
for group in groups:
  f.write("- groupName: ")
  f.write(group.groupName)
  f.write("\n")
  
  f.write("  category: ")
  f.write(group.category)
  f.write("\n")
  
  f.write("  objectType: ")
  f.write(group.objectType)
  f.write("\n")
  
  f.write("  objectName: ")
  f.write(group.objectName)
  f.write("\n")
  
  f.write("  fullPath: ")
  f.write(group.fullPath)
  f.write("\n")
    
f.close()