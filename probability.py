import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random

def Graph(number, probability, count_connected, count_euler):
    Vertex = set([v for v in range(number)])
    Edge = set()
    
    for combination in combinations(Vertex, 2):   
        # Defining a random variable
        var = random()
        
        if var < probability: # probability that edge exists
            Edge.add(combination)
            
   
    
    g = nx.Graph()
    
    g.add_nodes_from(Vertex)
    
    g.add_edges_from(Edge)
    euler = nx.is_eulerian(g)
    conn = nx.is_connected(g)
    
    # print("graph is connected? ", conn)
    
    if conn == True: 
        count_connected += 1
        if euler == True: 
            count_euler += 1
            # print(f"\nIs_connected: {conn}")
            # print(f"Is_Euler: {euler}")
            
            pos = nx.spring_layout(g)
    
            nx.draw_networkx(g, pos)
    
            plt.title("Random Graph ")
            plt.show()
    return count_connected, count_euler 
        
    
    


number = 10

probability = 0.4

count_euler = 0
count_connected = 0

for i in range(5000):
    count_connected, count_euler = Graph(number, probability, count_connected, count_euler) 
    # print(f" Number of connected graph {count_connected}, number of Euler circuit {count_euler}")

try:
    probability_of_euler = count_euler/count_connected
    print(f"The estimated probability of getting an euler given that the graph is connected is: {probability_of_euler}")
except ZeroDivisionError as e:
    print(e)
    
    
        
        


# print(generate_graph)

