import numpy as np
import re
import matplotlib.pyplot as plt

file_text = open('Wiki-Vote.txt' ,'r',encoding='ISO-8859-1').read()

temp = re.sub('[^0-9]',' ',file_text)
tokens = temp.split(' ')
ret = [int(i) for i in tokens if not i == '']

nodes = ret[1]
edges = ret[2]

ret = ret[2:]
ret = np.unique(ret)

node_to_index = {}
index_to_node = {}

num = 0
for i in ret:
    node_to_index[i] = num
    index_to_node[num] = i
    num += 1

lines = re.sub('[^0-9\n]',' ',file_text)
lines = lines.split('\n')
lines = [i.split(' ') for i in lines[4:] if not i == '']

graph = [[] for i in range(nodes)]

for i in range(edges):
    edge = lines[i]
    graph[node_to_index[int(edge[0])]].append(node_to_index[int(edge[1])])

print('Nodes: ' + str(nodes))

print('Edges: ' + str(edges))

max_edges = nodes * (nodes - 1)

in_degrees = [0 for i in range(nodes)]
for i in graph:
    for j in i:
        in_degrees[j] += 1
sum = 0
max_degree = -1
max_node = -1
for i in in_degrees:
    sum += i
    if i > max_degree:
        max_degree = i
        max_node = in_degrees.index(i)
print('Avg In-Degree: ' + str(sum/nodes))
print('Max In-Degree: ' + str(max_degree))
print('Max In-Degree Node: ' + str(max_node) + ' (Node Value - ' + str(index_to_node[max_node]) + ')')

sum = 0
max_degree = -1
max_node = -1
out_degrees = []
for i in graph:
    t = len(i)
    out_degrees.append(t)
    sum += t
    if t > max_degree:
        max_degree = t
        max_node = graph.index(i)
print('Avg Out-Degree: ' + str(sum/nodes))
print('Max Out-Degree: ' + str(max_degree))
print('Max Out-Degree Node: ' + str(max_node) + ' (Node Value - ' + str(index_to_node[max_node]) + ')')

print('Density of the Network: ' + str(edges / max_edges))

x = [i for i in range(nodes)]
n, bins, patches = plt.hist(x, nodes - 1)
plt.plot(bins, in_degrees, 'blue')
plt.xlabel('Nodes')
plt.ylabel('In-Degrees')
plt.title('In-Degree Distribution of Network')
plt.show()

plt.plot(bins, out_degrees, 'blue')
plt.xlabel('Nodes')
plt.ylabel('Out-Degrees')
plt.title('Out-Degree Distribution of Network')
plt.show()

clustering_coefficient = []
for i,j in zip(in_degrees,out_degrees):
    clustering_coefficient.append(i + j)
y = [0 for i in range(max(clustering_coefficient) + 1)]
for i in clustering_coefficient:
    y[i] += 1
x = [i/max_edges for i in range(len(y))]
n, bins, patches = plt.hist(x, len(y) - 1)
plt.plot(bins, y, 'blue')
plt.xlabel('Local Clustering Coefficient (Value)')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Distribution of Network')
plt.show()