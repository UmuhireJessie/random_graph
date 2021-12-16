"""
THE FOLLOWING PROGRAM IS GOING TO GENERATE THE GRAPH WITH TEN VERTICES BY USING
DIFFERENT PYTHON LIBRARIES, FOR INSTANCE MATPLOTLIB TO HELP USE US DRAW AND 
VISUALISE THE GRAPH. THE NETWORKX MODULE CREATE, MANIPULATE THE STRUCTURE OF 
THESE GRAPHS. BECAUSE WE HAVE BEEN ASKED TO GENERATE THE GRAPH RANDOMLY, WE 
IMPORTED RANDOM TO GENERATE RANDOM VALUE. ALSO, COMBINATION MODULE WAS USED TO 
COMBINE THE VERTICES TO KNOW THE EDGES. """


# Importing useful libraries

import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random


""" Defining a function, Graph(), that will help us to generate the graph 
randomly. It will take in two arguments, the number of vertices and 
the probability at which the edges will be produced."""          

def Graph(number, probability):
    # Creating a list of vertices which are in range of identified number.
    Vertex = set([v for v in range(number)])
    # Creating a set that will store Edges between vertices
    Edge = set()
    
    """ Since we have the list of vertices and a set of Edges, which empty so 
    far, wwe are going to use combination module to combine 2 vertices, 
    according to the identifies probability. """
    
    # Iterating through the combination of Vertex, the 2 means that we are 
    # creating edges between two verteces, hence passing 2
    for combination in combinations(Vertex, 2):
        # Defining a random variable
        var = random()
        if var < probability: 
            
            """ As we iterate, if the var is less than the probability, then we
            are going to add that pair of vertices in the set of edges. The var 
            here could be anything, so if we reach a point where the random 
            variable becomes greater than the probability, the program will do 
            nothing hence stopping the iteration. """
            
            Edge.add(combination)
    
    # Defining the graph, nx. is heping us to visualise the structure of graph
    g = nx.Graph()
    
    # Making the list of Vertex, the nodes of the graph
    g.add_nodes_from(Vertex)
    
    # Making the edges to be defined by the set of Edges gerated above
    g.add_edges_from(Edge)
    
    # Checking if the graph is connected
    conn = nx.is_connected(g)
    
    # Checking if the graph has an Euler circuit
    euler = nx.is_eulerian(g)
    print(f"\nIs_connected: {conn}")
    print(f"Is_Euler: {euler}")
    
    # Returning the graph
    return g

# Defining the number of verices. In this case, they are 10 vertices
number = 10

# Defining the probability at which to produce the edges between vertices
probability = 0.4
    
# Passing variable names to Graph function and storing it in a variable
generate_graph = Graph(number, probability)

# Defining the pos variable to store the positions of the nodes created using 
# nx.spring_layout function of networkx module.
pos = nx.spring_layout(generate_graph)

# Then after, we visualise the graph depending on the position of nodes given 
# above.
nx.draw_networkx(generate_graph, pos)

# The title of the graph and finally showing the graph
plt.title("Random Graph ")
plt.show()

