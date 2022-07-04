#!/usr/bin/env python
# coding: utf-8

# In[33]:


#create graph
import numpy as np
fread = open("directed graph.txt", "r")
G_v_e = fread.readline()
G_v_e = G_v_e.split(' ')
V = int(G_v_e[0])
E = int(G_v_e[1].strip())


# In[34]:


V_list = list(range(0,7,1))
lines = fread.readlines()
A_dict = {}
for line in lines:
    t_h = line.split(' ')
    tail = int(t_h[0])
    if tail in A_dict.keys():
        A_dict[tail].append(int(t_h[1].strip()))
    else:
        A_dict[tail] = [int(t_h[1].strip())]
#print(A_dict)


# In[35]:


def remove(original, visited):
    modified = original
    for i in visited:
        try: 
            modified.remove(i)
        except ValueError:
            pass
    return modified


# In[36]:


#implementing DFS
# search function
def search(j, visited, traversal, A_dict):
    if j not in A_dict.keys():
        return
    connected = remove(A_dict[j], visited)
    #print(connected)
    visited.extend(connected)
    #print(visited)
    for k in connected:
        #print(k)
        traversal.append(k)
        #print("traversal ", traversal)
        search(k, visited, traversal, A_dict)
    return


# In[37]:


#G = V, A_dict, start_node
s = 0
visited = [s]
traversal = visited.copy()
search(s, visited, traversal, A_dict)
#print(traversal)
if (len(visited) == V):
    print(traversal)
else:
    remaining = remove(V_list, traversal) 
    print(remaining, " nodes not reachable")
    


# In[ ]:
fread.close()

#%%



