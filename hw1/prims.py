#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prims.py
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


class uwGraph:
  __num_edges = 0
  __num_nodes = 0
  __graph_edges = {}
  __graph_nodes = []
  __A = {}
  __max_wt = 0
  
  def __init__(self):
    __num_edges = 0
    __num_nodes = 0
    __graph_edges = {}
    __A = {}
  
  def readGraph(self, filename):
    gFile = open(filename)
    
    for line in gFile:
      if self.__num_nodes == 0:
        nodes, edges = line.split()
        self.__num_nodes = int(nodes)
        self.__num_edges = int(edges)
      else:
        start, end, wt = line.split()
        start = int(start)
        end = int(end)
        wt = int(wt)
        
        if wt > self.__max_wt:
          self.__max_wt = wt
        
        if not start in self.__graph_edges:
          self.__graph_edges[start] = []
          self.__graph_nodes.append(start)
        
        if not end in self.__graph_edges:
          self.__graph_edges[end] = []
          self.__graph_nodes.append(end)
        
        self.__graph_edges[start].append((end, wt))
        self.__graph_edges[end].append((start, wt))
  
  def nodes(self):
    return self.__graph_nodes
    
  def prims_mst(self, start):
    
    unprocessed = self.__graph_nodes
    processed = [start]
    unprocessed.remove(start)
    count = 1
    cost = 0
    while len(unprocessed) > 0:
      min_wt = self.__max_wt
      next_node = -1
      for node in processed:
        for end, wt in self.__graph_edges[node]:
          if not end in processed:
            if wt <= min_wt:
              min_wt = wt
              next_node = end
      processed.append(next_node)
      unprocessed.remove(next_node)
      count += 1
      cost += min_wt
      print next_node
    print cost

def main():
  script, fileName = argv
  testGraph = uwGraph()
  testGraph.readGraph(fileName)
  testGraph.prims_mst(testGraph.nodes()[0])
  
  return 0

if __name__ == '__main__':
  main()

