#!/usr/bin/env python3
  
import json

class Group:
  def __init__(self, batch, groupName, permRepName):
    self.batch = batch
    self.groupName = groupName
    self.permRepName = permRepName

print("Reading theta.json")


print("Generated groups.yml successfully")