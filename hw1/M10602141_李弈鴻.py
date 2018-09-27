
# coding: utf-8

# In[38]:


import csv
from igraph import *

g = Graph();

'''input vertices'''
with open('node_information.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    i = 0
    for row in rows:
        g.add_vertices(1)
        g.vs[i]["id"] = row[0]
        i = i + 1 

'''add edges'''
with open('Period1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    k = 0
    for row in rows:
        source_v = g.vs.find( id = row[1] )
        target_v = g.vs.find( id = row[2] )
        g.add_edges([( int(source_v.index), int(target_v.index) )])
        print('link: ' + str(k))
        k = k + 1

'''find shortest path'''
for a in range( 0, 27770):
    with open( str(a) + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for b in range( 0, 27770):
                if a != b :
                    #print( 'source: ' + g.vs[a]["id"] + ' target: ' + g.vs[b]["id"] + ' shortest: ' + str(g.shortest_paths_dijkstra( a, b, None, OUT)[0]))
                    writer.writerow([g.vs[a]["id"], g.vs[b]["id"], str(g.shortest_paths_dijkstra( a, b, None, OUT)[0])])
print( 'done' )
#print( g.shortest_paths_dijkstra( 24790, 26896, None, OUT)[0] )
#print(g.get_edgelist()[0:10] )


# In[4]:


with open('Period1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        source_v = g.vs.find( id = row[1] )
        target_v = g.vs.find( id = row[2] )
        g.add_edges(( source_v.index, target_v.index ))

