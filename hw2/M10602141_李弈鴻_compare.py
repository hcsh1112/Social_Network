
# coding: utf-8

# In[25]:


import csv

def search( node1, node2):
    node1_group = 0
    with open('output.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        # find node1 group
        for row in rows:
            if row :
                if int(row[0]) == node1 :
                    node1_group = int(row[1])
                    # get node1 group
        if node1_group == 0 :
            return int(1)
                    
    with open('output.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        # find node2 group
        for row in rows:
            if row:
                if int(row[0]) == node2:
                    if node1_group == int(row[1]):
                        return int(1)
                    elif node1_group <= int(row[1]) + 10 and node1_group >= int(row[1]) - 10:
                        return int(1)
                    else:
                        return int(0)
        return int(1)

with open( 'a.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in open('question.txt', 'r', encoding='UTF-8'):
        cut = i.split( "," )
        id_ = cut[0]
        n1 = int(cut[1])
        n2 = int(cut[2])
        writer.writerow([id_, str(search( n1, n2))])



# In[18]:




