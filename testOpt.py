# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""


from tme1opt import *
import time 
#from pympler import asizeof
files = ["amazon", "livejournal"]
for f in files:
    #creating EdgeList and AdjArray (also AdjMatrix but it's not scalable so it's commented out)
    start = time.time()
    g = Graph(f)
    l = g.mkEdgeList()
    #m = g.mkAdjMatrix(l)
    end = time.time()
    print("creating EdgeList time is: "+ str(end-start))
    
    start = time.time()
    m = g.mkAdjMatrix(l)
    end = time.time()
    print("creating AdjMatrix time is: "+ str(end-start))
    
    start = time.time()
    a = g.mkAdjArray(l)
    end = time.time()
    print("creating AdjArray time is: "+ str(end-start)+"\n")
    
    
    
    # running the bfs algorithm
    start = time.time()
    bfs = BFS()
    d = bfs.mkBfs(a,1)
    end = time.time()
    print("bfs time is: "+ str(end-start)+"\n")
    
    #finding the lower bound
    start = time.time()
    low = bfs.lowerBound(a, 1)
    print("lower bound: "+ str(low))
    end = time.time()
    print("lower bound time is: "+ str(end-start)+"\n")
    
    #finding the upper bound
    start = time.time()
    up = bfs.upperBound(a, 1)
    print("upper bound: "+ str(up))
    end = time.time()
    print("upper bound time is: "+ str(end-start)+"\n")
    
    
    a2 = g.mkadjarray2(l)
    
    #finding triangles
    start = time.time() 
    nTriangles = bfs.findTriangles(l, a2)
    print("number of triangles: "+ str(nTriangles))
    end = time.time()
    print("finding triangles time is: "+ str(end-start)+"\n")
    
    
    #various memory tests
    # print("size of edge list is is: "+ str(asizeof.asizeof(l)))
    # print("size of adjacency array is is: "+ str(asizeof.asizeof(a)))
    
    #print methodes for data structures
    # g.print_edges(l)
    # g.print_matrix(m)
    # g.print_adjarray(a)