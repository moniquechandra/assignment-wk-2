import networkx as nx
import random
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Exercise 3.1

# Define the parameters: n0, N, and M
n0 = 5
G = nx.star_graph(n0)
N = 400 # total webpage
M = 4 # number of links for every new webpage
degrees = dict(G.degree()).values() # dictionary of each existing node's degrees
total_degree = sum(degrees)
# Add additional nodes until it is N
for i in range(n0, N):
    G.add_node(i)

# Calculate the probabilities (p_i) for each node based on its degree (d_i)
    p_i = {} 
    for node in G.nodes():
        degree = G.degree(node)
        p_i[node] = degree / total_degree

# Ensure no pages link to themselves
G.remove_edges_from(nx.selfloop_edges(G))

# Choose the pages to link to based on the probabilities
for node in G.nodes():
    neighbors = list(G.neighbors(node))
    while len(neighbors) < M:
        random_node = random.choices(list(p_i.keys()), weights=list(p_i.values()), k=1)[0]
        if random_node != node and random_node not in neighbors:
            neighbors.append(random_node)
            G.add_edge(node, random_node)

nx.draw(G, node_color = 'blue',node_size = 100)
plt.show()

###
            
# Exercise 3.2

# Create a directed graph from 'squirrel_edges.csv'
G2 = nx.DiGraph()

# Read the CSV file and add the edges to the graph
with open('squirrel_edges.csv', 'r') as file:
    for line in file:
        source, target = line.strip().split(';')
        G2.add_edge(source, target)

# Calculate PageRank
pagerank = nx.pagerank(G2)

# Visualize the PageRank distribution
plt.figure(figsize=(10, 6))
plt.hist(list(pagerank.values()), bins=30, alpha=0.7, color='b', edgecolor='k')
plt.title('PageRank Distribution')
plt.xlabel('PageRank Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
