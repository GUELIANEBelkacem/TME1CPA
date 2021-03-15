# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""
from collections import defaultdict
import random
class Edge:
    __slots__ = 'x', 'y'
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    
class Node:
    __slots__ = 'idn', 'neighbours'
    def __init__(self, idn):
        self.idn = idn
        self.neighbours = []

        
    def copyn(self):
        n= Node(self.idn)
        n.neighbors = self.neighbors[:]
        return n
    @property
    def d(self):

        return len(self.neighbours)

    
        
        
class Graph:
    """ class Graph(String s) takes the path to the .txt file containing a list of edges.
        \n contains methids for generating an Edge List, an Adjacency Matrix and/or 
        an Adjacency Array, along with print methodes for all 3 data structures"""
    def __init__(self, s):
        self.s = s
        
    #data structure makers--------------------------------------------------
    
    def mkEdgeList(self):
        """ mkEdgeList() makes an edge list from the given .txt file inserted when creating an instance of Graph""" 
        listy = []
        f = open(self.s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            e = Edge(int(temp[0]), int(temp[1]))
            listy.append(e)
        f.close()
        print("number of edges: " + str(self.nedges(listy)))
        print("number of nodes: " + str(self.nnodes(listy))+"\n\n")
        return listy
    
    
    
    
    # def mkAdjMatrix(self, l):
    #     """ mkAdjMatrix(EdgeList l) makes an adjacincy matrix from a given edge list""" 
    #     n = self.nnodes(l)
    #     matrix = [ [ 0 for i in range(n) ] for j in range(n) ] 
    #     for e in l:
    #         matrix[e.x][e.y] = 1
    #     return matrix
    
    def mkAdjMatrix(self, l):
        """ mkAdjMatrix(EdgeList l) makes an adjacincy matrix from a given edge list""" 
        n = self.nnodes(l)
        # matrix = [ [ 0 for i in range(n) ] for j in range(n) ] 
        matrix = {}
        for i in range(n):
            matrix[i] = defaultdict(int)
        for e in l:
            matrix[e.x][e.y] = 1
        return matrix
    
    
    def mkAdjArray(self,l):
        """ mkAdjArray(EdgeList l) makes an adjacincy array from a given edge list""" 
        
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)
            listy[k.y].neighbours.append(k.x)
        return listy
    

    
    
    def mkadjarray2(self, l):
        """ mkAdjArray2(EdgeList l) makes an adjacincy array from a given edge list 
        with the particulatity of it turned into a directed graph 
        (useful for detecting triangles)""" 
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)

        return listy
    
            
    #support functions------------------------------------------------------                     
    def nedges(self,listy):
        return len(listy)
    def nnodes(self,listy):
        s= 0
        for n in listy:
            if(s<n.x):
                s=n.x
            if(s<n.y):
                s=n.y
        return s+1
    
    #prints-----------------------------------------------------------------
    def print_edges(self, listy):
        f = open("EdgeList.txt", "w")
        for e in listy:
            f.write(str(e.x)+"   "+str(e.y)+"\n")
        f.close()    
    def print_matrix(self, matrix):
        f = open("AdjMatrix.txt", "w")
        s = ""
        f.write("the adjacency matrix:\n")
        s = ""
        for i in matrix:
            for j in i:
                s= s+(str(j) + " ")
            s= s+("\n")
            f.write(s)
        
        f.close() 
        
    def print_adjarray(self, listy):
        f = open("AdjArray.txt", "w")
        s = ""
        print("the adjacency array:\n")
        for i in listy:
            n = listy[i]
            s = ""
            s = s+str(n.idn)+" -> "            
            for neighbour in n.neighbours:
                s = s+str(neighbour)+" -> "
            s = s+"/\n"
            f.write(s)
            #print(s)
        f.close()
        

        
        
class BFS:
    
    def __init__(self):

        self.sss=""
        
        
    def mkBfs(self, al, start):
        """ mkBfs(EdgeList l, Int start) return a tuple(x,y,d):\n
        x: the diameter of the graph starting from 'start'\n
        y: the furthest node from the node 'start'\n
        d: a dictionary <Int node, Int distance_from_start>""" 
        done = []
        pending = []
        l={}
        d={}
        for i in range(len(al)):
            l[i]=False
            d[i]=0
        lower  = 0
        lowern = 1
        
        x = start
        l[x] = True
        pending.append(start)
        
        while(pending):
            temp = pending.pop(0)
            done.append(temp)
            dist = d[temp]
            for n in al[temp].neighbours:
                if(not(l[n])):
                    l[n] = True
                    d[n] = dist+1
                    if(dist+1>=lower):
                        lower = dist+1
                        lowern = n
                        pending.append(n)
        d[start] = -1
        return (lower, lowern, d)
        
    def lowerBound(self,al,start):
        """ lowerBound(EdgeList l, Int start) returns 
        the lower bound of the diameter of the graph""" 
        lowersNoads = []
        lowers = []
        low = start
        for i in range(5):
            x = self.mkBfs(al,low)
            low = x[1]
            lowersNoads.append(low)
            lowers.append(x[0])
        return max(lowers)
        
    def upperBound(self,al,start):
        """ upperBound(EdgeList l, Int start) returns 
        the upper bound of the diameter of the graph""" 
        bfs = self.mkBfs(al,start)

        mid = bfs[0]//2
        #print("mid " +str(mid))
        midn = start
        i = 0
        si = len(bfs[2])
        while(i<si):
            if(bfs[2][i] == mid):
                midn = i
                break
            i = i +1
        
        #print("mid node and dist ["+str(midn)+","+str(mid)+"]")
        upperNoads = []    
        upper = []

        bfs = self.mkBfs(al,midn)
        upperNoads.append(bfs[1])
        upper.append(bfs[0])
        temp = bfs[1]
        tempn = al[bfs[1]] 
        al[bfs[1]] = Node(bfs[1])

        bfs = self.mkBfs(al,midn)
        upperNoads.append(bfs[1])
        upper.append(bfs[0])
        
        al[temp] = tempn
        # print("the two furthest nodes from the mid and their dist")
        # print(upperNoads)
        # print(upper)
        # print("the upper bound:")
        # print(upper[0]+upper[1])
        return upper[0]+upper[1]
    
        
    def findTriangles(self,e,a):
        """ lowerBound(EdgeList e, AdjArray a) where a is an optimised AdjArray
        generated by Grapbh.mkAdjArray2, returns the number of triangles in the graph""" 
        count=0
        #w = []
        for ee in e:
            for x in a[ee.x].neighbours:
                for y in a[ee.y].neighbours:
                    
                    if(x == y):
                        #w.append((ee.x,ee.y,x))
                        count = count+1    
        #print(w)                
        return count



        
        