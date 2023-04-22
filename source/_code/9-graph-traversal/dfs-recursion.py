graph = {
    "v1": ["v2", "v3", "v4"],
    "v2": ["v1", "v5", "v6"],
    "v3": ["v1"],
    "v4": ["v1", "v6"],
    "v5": ["v2"],
    "v6": ["v2", "v4"],
}

visited = []


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, "v1")
print(visited)
