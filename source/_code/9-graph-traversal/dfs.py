from collections import deque

graph = {
    "v1": ["v2", "v3", "v4"],
    "v2": ["v1", "v5", "v6"],
    "v3": ["v1"],
    "v4": ["v1", "v6"],
    "v5": ["v2"],
    "v6": ["v2", "v4"],
}

visited = []
stack = deque()


def dfs(graph, node):

    stack.append(node)
    while len(stack) > 0:

        node = stack.pop()
        if node not in visited:
            visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


dfs(graph=graph, node="v1")
print(visited)
