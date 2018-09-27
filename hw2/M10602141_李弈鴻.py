
# coding: utf-8

# In[7]:


from igraph import *
import csv

g = Graph()

'''total 1005 node'''
for i in range(0, 1006):
    g.add_vertices(1)
    g.vs[i]["id"] = i
    
for i in open('email-Eu-core.txt', 'r', encoding='UTF-8'):
    cut = i.split()
    g.add_edges([( int(cut[0]), int(cut[1]) )])
    g.es["width"] = 1

temp = g.community_edge_betweenness(directed=True)
clusters = temp.as_clustering()
group = clusters.membership

with open( 'output3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for name, membership in zip(g.vs["id"], group):
        writer.writerow([name, membership])

