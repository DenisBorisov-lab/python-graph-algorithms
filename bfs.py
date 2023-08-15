graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []
queue = []


def bfs(graph, visited: list, node):
    visited.append(node)
    queue.append(node)

    while queue:
        n = queue.pop(0)
        print(n, end=" ")
        for elem in graph[n]:
            if elem not in visited:
                visited.append(elem)
                queue.append(elem)


bfs(graph, visited, "5")
