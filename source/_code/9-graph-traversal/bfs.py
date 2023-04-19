graph = {
    "v1": ["v2", "v3", "v4"],
    "v2": ["v1", "v5", "v6"],
    "v3": ["v1"],
    "v4": ["v1", "v6"],
    "v5": ["v2"],
    "v6": ["v2", "v4"],
}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, "v1")  # function calling
print(visited)
