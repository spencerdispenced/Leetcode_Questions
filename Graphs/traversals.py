

def dfs(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


def bfs(graph, source):
    queue = [source]

    while len(queue) > 0:
        current = queue.pop()
        print(current)

        for neighbor in graph[current]:
            queue.insert(0, neighbor)


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


if __name__ == '__main__':
    #dfs(graph, 'a')
    bfs(graph, 'a')
