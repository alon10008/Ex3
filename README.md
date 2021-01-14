# Ex3
  
  - data folder path is: Ex3/src/data
  
    all the files name in the code adjust to this path!

## DiGraph:
   
   - class Node:
   
     This class represent vertex, and include the vertex id, his position and a dict of his neighbors.
     
   - class Edge:
     
     this class represent edge, and include the source and destination vertices id's and his weight.
     
   - class pos:
     
     This class represent 3D location(point), include tuple (x,y,z).
     
   - class DiGraph:
     
     This class represent direcdet weighted graph. 
     Class variable:
     
     ```python
     self.mc = 0
     self.edges = {}
     self.nodes = {}
     ```
     Function edge_key: make key for each edge in "edges" dict.
     
     ```python
     def edge_key(self, e):
         return e.src*17.17 + e.dst*19.19 + e.weight*23.23
     ``` 
     
## GraphAlgo:   
   
   - class AlgoGraph:
     
     Class variable:
     
     ```python
     self.g = DiGraph()
     self.counter = 0
     ```
     
     Class functions:
     
     - connected_components: based on Tarjan's algorithm. Iterative DFS version.
     
     - connected_component: use connected_components to find the id's component. 
     
     - Shortest_path: based on dijkstra's algorithm.
     
     - tarjan: iterative version of SCC tarjan algorithm.
     
     - DFS: recursion version of SCC tarjan algorithm.
     
     - range: find the x and y boundaries of the nodes.
     
     - check: check for node if the function check all of his neighbors. Used in tarjan().
     
     
     
 ## Part 3:
   
   ### G_10_80_1.json
     
     
   | Algorithm | python | networkx | java |
   | --- | --- | --- | --- |
   | connected_components | 0[millisec] | 0[millisec] | 0[millisec] |
   | connected componnet | 0[millisec] | ---------- | 0[millisec] |
   | shortest_path | 0[millisec] | 0[millisec] | 1[millisec] |
   
   ### G_100_800_1.json
   
   | Algorithm | GraphAlgo | networkx | java |
   | --- | --- | --- | --- |
   | connected_components | 1[millisec] | 0[millisec] | 2[millisec] |
   | connected componnet | 1[millisec] | ---------- | 2[millisec] |
   | shortest_path | 3[millisec] | 0[millisec] | 2[millisec] |
   
   ### G_1000_8000_1.json
   
   | Algorithm | GraphAlgo | networkx | java |
   | --- | --- | --- | --- |
   | connected_components | 18[millisec] | 1[millisec] | 15[millisec] |
   | connected componnet | 19[millisec] | ---------- | 20[millisec] |
   | shortest_path | 22[millisec] | 6[millisec] | 17[millisec] |
   
   ### G_10000_80000_1.json
   
   | Algorithm | GraphAlgo | networkx | java |
   | --- | --- | --- | --- |
   | connected_components | 202[millisec] | 0[millisec] | 55[millisec] |
   | connected componnet | 202[millisec] | ---------- | 49[millisec] |
   | shortest_path | 259[millisec] | 100[millisec] | 79[millisec] |
   
   ### G_20000_160000_1.json
   
   | Algorithm | GraphAlgo | networkx | java |
   | --- | --- | --- | --- |
   | connected_components | 405[millisec] | 0[millisec] | 80[millisec] |
   | connected componnet | 408[millisec] | ---------- | 81[millisec] |
   | shortest_path | 568[millisec] | 47[millisec] | 184[milisec] |
   
   ### G_30000_240000_1.json
   
   | Algorithm | GraphAlgo | networkx | java |
   | --- | --- | --- | --- |
   | connected_components | 636[millisec] | 0[millisec] | 68[millisec] |
   | connected componnet | 634[millisec] | ---------- | 73[millisec] |
   | shortest_path | 924[millisec] | 406[millisec] | 428[millisec] |
   
   
 ## Main.py
    
    This file include the ex3_main.py and main() function that tests the functions runtime.
    - shortest_path() the path between the first node - 0 and the last node - (v_size-1).
    - connected_component() find the component of the first node - 0.
    
   
 ## System
 
    processor: AMD Ryzen 7 1700 Eight-Core Processor.
    RAM: 16.0 GB
    Windows10-64
   
   
