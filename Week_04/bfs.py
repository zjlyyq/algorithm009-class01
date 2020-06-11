def bfs(graph, start, end):
    queue = []
    queue.append(start)
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        # process node
        
        for node in generate_related_node(node):
            if node not in visited:
                queue.append(node)

def generate_related_node(node):
    return []