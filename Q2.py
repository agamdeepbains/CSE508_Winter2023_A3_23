import numpy as np
import re
import networkx as nx
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

G = nx.DiGraph()

for i in range(edges):
    edge = lines[i]
    G.add_edge(node_to_index[int(edge[0])], node_to_index[int(edge[1])])

pagerank_scores = nx.pagerank(G)
pagerank_scores = [pagerank_scores[i] for i in range(nodes)]

hits_scores = nx.hits(G)
authority_scores = [hits_scores[0][i] for i in range(nodes)]
hub_scores = [hits_scores[1][i] for i in range(nodes)]

x = [i for i in range(nodes)]
plt.plot(x, pagerank_scores, 'blue')
plt.xlabel('Nodes')
plt.ylabel('Scores')
plt.title('PageRank Scores of Network Nodes')
plt.show()

plt.plot(x, authority_scores, 'blue')
plt.plot(x, hub_scores, 'red')
plt.xlabel('Nodes')
plt.ylabel('Scores')
plt.title('Authority (Blue) and Hub (Red) Scores of Network Nodes')
plt.show()