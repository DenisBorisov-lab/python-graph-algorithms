graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()

def dfs(graph, visited, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for elem in graph[node]:
            dfs(graph, visited, elem)

dfs(graph, visited, "5")
