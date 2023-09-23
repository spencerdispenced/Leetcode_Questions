

def has_path_dfs(graph, src, dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path_dfs(graph, neighbor, dst):
            return True
    return False


def has_path_bfs(graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        current = queue.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.insert(0, neighbor)
    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

if __name__ == '__main__':
    #print(has_path_dfs(graph, 'g', 'i'))
    print(has_path_bfs(graph, 'f', 'k'))
