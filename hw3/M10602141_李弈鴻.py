
# coding: utf-8

# In[4]:


import csv

with open( 'hw3infmax.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    node = -1 
    degree = 0
    sum_weight = 0.0
    avg_weight = 0.0
    with open( 'output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['node', 'degree', 'avg_weight'])
        for row in rows:
            if node == -1:
                node = int(row[0])
                degree = 1
                sum_weight = float( row[2] )
            elif node != int( row[0] ):
                avg_weight = sum_weight / degree
                writer.writerow([str(node), str(degree), str(avg_weight)])
                print( 'node: ' + str(node) + ' degree: ' + str(degree) + ' avg_weight: ' + str(avg_weight) )
                node = int(row[0])
                degree = 1
                sum_weight = float( row[2] )
            else :
                degree = degree + 1
                sum_weight = sum_weight + float(row[2])


# In[43]:


with open( 'output2.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    all_list = []
    i = 0 
    degree = 0
    for row in rows:
        all_list.append([])
        all_list[i].append(row[0])
        degree = int(row[1])
        with open( 'output2.csv', 'r', newline='') as csvfile:
            rows_2 = csv.reader(csvfile)
            for row_2 in rows_2:
                if row[0] != row_2[0]:
                    if int(row_2[1]) + degree <= 50:
                        degree = degree + int(row_2[1])
                        all_list[i].append(row_2[0])
                    else:
                        break
        
        i = i + 1

    with open( 'vector2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for j in range(0, i):
            string = ""
            for k in range(0, len(all_list[j])):
                if k != len(all_list[j]) - 1 :
                    string = string + all_list[j][k] + ","
                else :
                    string = string + all_list[j][k]
                
            writer.writerow([string])
            


# In[66]:


def Get_degree( _id, level ):
    if int(level) == 2 :
        return int(1)
    else :
        total = int(0)
        with open( 'hw3infmax.csv', 'r', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if int(row[0]) == int(_id):
                    total = total + Get_degree( int(row[1]), int(level)+1 )
            return int(total)
'''
with open( 'output2.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    a = 0
    for row in rows:
        temp = row[0].split(',')
        list_t = list(temp)
        total_degree = int(0)
        with open( 'output_5level.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(0, len(list_t)):
                total_degree = total_degree + Get_degree(str(list_t[i]), int(0))
            writer.writerow([a, total_degree])
        a = a + 1
'''
with open( 'output_3level_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    with open( 'output2.csv', 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)
        a = 0
        for row in rows:
            node = row[0]
            int_degree = row[1]
            total_degree = int(0)
            for i in range(0, len(list_t)):
                total_degree = total_degree + Get_degree(node, int(0))
            writer.writerow([node, int_degree, total_degree])
            print(a)
            a = a + 1

