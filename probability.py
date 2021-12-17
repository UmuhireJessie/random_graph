import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random

""" Defining a function, Graph(), that will help us to generate the graph 
randomly. It will take in two arguments, the number of vertices and 
the probability at which the edges will be produced."""


def Graph(number, probability, count_connected, count_euler):
    # Creating a set to store a list of vertices which are in range of
    # identified number.
    # created some variable such as count_connected and count_euler which will be used
    # to find the probability of getting a an euler circuit
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

        if var < probability:  # probability that edge exists
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

    # create variable euler and stored a bool value of nx.is_eulerian(g)
    euler = nx.is_eulerian(g)
    # created variable conn and stored a bool value of nx.is_connected(g)
    conn = nx.is_connected(g)

    # created an if condition to check if variable conn is True w
    # which means that our graph is connected
    if conn == True:
        # after the condition is True we increment our count_connected variable by 1
        count_connected += 1

        # created another if condition to check if variable euler is True
        # which means that our graph has an euler circuit
        if euler == True:
            # after the condition is True we increment our count_euler variable by 1
            count_euler += 1

            # the code nx.spring_layout position the node of our graph using Fruchterman-Reingold force-directed algorithm
            pos = nx.spring_layout(g)

            # the code nx.draw_networks draws the graph
            nx.draw_networkx(g, pos)

            # create a title for our graph on matplot
            plt.title("Random Graph ")
            
            # shows/displays our graph on matplot
            plt.show()
    return count_connected, count_euler


# initiate the number nodes we start with
number = 10

# this is a probability of producing edges
probability = 0.4

# initiate our count variable to 0
count_euler = 0
count_connected = 0

# created a for loop to run our function many times
# we gave it a large range of 5000 because it was hard to continualy running the program until you get a euler circuit
for i in range(5000):
    # code to run the function
    count_connected, count_euler = Graph(number, probability, count_connected, count_euler)
    # print(f" Number of connected graph {count_connected}, number of Euler circuit {count_euler}")

# we handle exceptions so that our program to could not terminate itself in middle with out completing if we have zero number of graphs connected
try:
    # calculate the probability of getting a graph with euler circuit given the graph is connected
    probability_of_euler = count_euler/count_connected
    print(f"\n\tThe estimated probability of getting an euler given that the graph is connected is: {probability_of_euler}")

# thrown an exception when count_connected is zero, as we can't divide a number by zero
except ZeroDivisionError as error:
    print(error)
