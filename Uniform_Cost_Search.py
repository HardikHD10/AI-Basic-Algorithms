import heapq

def uniform_cost_search(graph, start, goal):
    # Create a priority queue and add the start node with a cost of 0
    queue = [(0, start)]
    # Create a dictionary to store the cost of each node
    cost = {start: 0}
    # Create a dictionary to store the parent of each node
    parent = {start: None}
    # Create a set to store the visited nodes
    visited = set()

    while queue:
        # Pop the node with the lowest cost from the queue
        current_cost, current_node = heapq.heappop(queue)
        # If the current node is the goal, return the path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]
        # If the current node has already been visited, skip it
        if current_node in visited:
            continue
        # Mark the current node as visited
        visited.add(current_node)
        # Loop through the neighbors of the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # If the neighbor has not been visited
            if neighbor not in visited:
                # Calculate the total cost to reach the neighbor
                total_cost = current_cost + neighbor_cost
                # If the neighbor is not in the cost dictionary or the new cost is lower than the previous cost
                if neighbor not in cost or total_cost < cost[neighbor]:
                    # Update the cost and parent of the neighbor
                    cost[neighbor] = total_cost
                    parent[neighbor] = current_node
                    # Add the neighbor to the queue with its updated cost
                    heapq.heappush(queue, (total_cost, neighbor))
    # If the goal is not reached, return None
    return None

graph = {
    'S': {'A': 5, 'B': 9, 'D':6},
    'A': {'G1': 9, 'B':3},
    'B': {'C': 1},
    'C': {'F': 7,'G2':5},
    'D':{'E':2,'C':2},
    'E': {'G3':7},
    'F': {'D':2,'G3':8},
    'G1':{},
    'G2':{},
    'G3':{}
}

graph1 = {
    'A': {'B':1,'C':3,'D':2},
    'B': {'A':1,'D':4,'E':1},
    'C': {'A':3,'D':2},
    'D': {'E':1,'F':1,'G1':5},
    'E': {'D':1,'F':3,'G2':2},
    'F': {'E':3,'G2':2,'G1':2,'G3':2},
    'G1':{'F':2,'D':5},
    'G2':{'E':2,'F':2},
    'G3':{'F':2}
}

start = 'S'
goal = 'G2'
print(uniform_cost_search(graph, start, goal))

start1 = 'A'
goal1 = 'G3'
print(uniform_cost_search(graph1, start1, goal1))