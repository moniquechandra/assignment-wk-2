import networkx as nx
import random
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def barabasi_albert_network(n0, N, M):
    """ 
    Ask for n0 (number of initial nodes), N (total webpages), and M (links for each node),
    and return a star network graph & a visualisation of PageRank's distribution.
    """
    # Define the parameters: n0, N, and M
    G = nx.star_graph(n0)
    
    # Add additional nodes until it is N
    for i in range(n0, N):
        new_node = i + len(G)
        # Calculate probabilities based on node degrees
        node_probabilities = [G.degree(node) for node in G.nodes()]
        node_probabilities = [prob / sum(node_probabilities) for prob in node_probabilities]
        # Sample M nodes to connect to
        targets = np.random.choice(list(G.nodes()), size=M, replace=False, p=node_probabilities)
        G.add_node(new_node)
        for target in targets:
            G.add_edge(new_node, target)
    
    # Ensure no pages link to themselves
    G.remove_edges_from(nx.selfloop_edges(G))

    # Calculate PageRank
    pagerank = nx.pagerank(G)

    # Draw the network
    plt.subplot(121)
    nx.draw(G, node_color = 'blue',node_size = 100)
    plt.title('Generated Barabasi-Albert Network')

    # Visualize the distribution of PageRank probabilities
    plt.subplot(122)
    pagerank_list = list(pagerank.values())
    plt.hist(pagerank_list, bins=20, alpha=0.5, color='b', edgecolor='black')
    plt.xlabel('PageRank Probability')
    plt.ylabel('Frequency')
    plt.title('Distribution of PageRank Probabilities')

    plt.tight_layout()
    plt.show()

###
            
def squirrel_edges(f):
    """ 
    Ask for a CSV file and return a visualisation of PageRank's distribution.
    """
    # Create a directed graph
    G2 = nx.DiGraph()

    # Read the CSV file and add the edges to the graph
    with open(f, 'r') as file:
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
