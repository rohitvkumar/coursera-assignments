#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scheduling.py
#  
#  Copyright 2015 Rohit Valsakumar <rohit@rohit-Vostro-270s>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from sys import argv

num_jobs = 0
job_list = []

class Job:
  __weight = -1
  __length = -1
  __index  = -1
  
  def __init__(self, ix, wt, ln):
    self.__index  = int(ix)
    self.__weight = int(wt)
    self.__length = int(ln)
    
  def __cmp__(self, other):
    val1 = self.__weight - self.__length
    val2 = other.__weight - other.__length
    
    if val1 == val2:
      return other.__weight - self.__weight
    else:
      return val2 - val1
      
  def __str__(self):
    return str((self.__index, self.__weight, self.__weight - self.__length))
    
  def weight(self):
    return self.__weight
    
  def length(self):
    return self.__length

def readJobsFromFile(fileName):
  
  global num_jobs
  global job_list
  
  file = open(fileName)
  index = 0
  for line in file:
    if num_jobs == 0:
      num_jobs = int(line)
    else:
      wt, ln = line.split()
      job_list.append(Job(index, wt, ln))
      #print job_list[index]
      index += 1
      
def weightedCompletionTime():
  global job_list
  completionTimeSum = 0
  weightTime = 0
  
  for job in sorted(job_list):
    print job
    completionTimeSum += job.length()
    weightTime += job.weight() * completionTimeSum
  
  return weightTime

def main():
  script, filename = argv
  readJobsFromFile(filename)
  
  print weightedCompletionTime()
  return 0

if __name__ == '__main__':
  main()
