from collections import defaultdict

def create_tree(graph):
    visited = set()
    tree = defaultdict(list)

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                tree[node].append(child)
                dfs(child)
    for node in graph:
        dfs(node)
    return dict(tree)

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

# graph = {
#     'A': {'B':1,'C':3,'D':2},
#     'B': {'A':1,'D':4,'E':1},
#     'C': {'A':3,'D':2},
#     'D': {'E':1,'F':1,'G1':5},
#     'E': {'D':1,'F':3,'G2':2},
#     'F': {'E':3,'G2':2,'G1':2,'G3':2},
#     'G1':{'F':2,'D':5},
#     'G2':{'E':2,'F':2},
#     'G3':{'F':2}
# }

# graph = {
#     'A': [('B', 10), ('C', 4)],
#     'B': [('A', 10), ('D', 6), ('C', 4)],
#     'C': [('A', 4), ('B', 4), ('E', 6)],
#     'D': [('B', 6), ('E', 6), ('F', 4)],
#     'E': [('C', 6), ('D', 6), ('G', 14)],
#     'F': [('D', 4), ('G', 4)],
#     'G': [('E', 14), ('F', 4)],
# }

tree = create_tree(graph)
print(tree)
