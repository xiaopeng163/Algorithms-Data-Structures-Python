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


def bfs(graph, node):  # function for BFS

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


bfs(graph=graph, node="v1")

print(visited)
