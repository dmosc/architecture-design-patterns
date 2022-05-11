from typing import List


def bfs(graph, start, end) -> (bool, List[int]):
    path = []
    visited = [start]
    while len(visited):
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                print(path)
                return True, path
            if current not in graph:
                continue
        visited = visited + graph[current]
    return False, path


def dfs(graph, start, end) -> (bool, List[int]):
    path = []
    visited = [start]
    while len(visited):
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                print(path)
                return True, path
            if current not in graph:
                continue
        visited = graph[current] + visited
    return False, path


def traverse(graph, start, end, action):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                return True, path
            if current not in graph:
                continue
        visited = action(visited, graph[current])
    return False, path


def extended_bfs_path(visited, current):
    return visited + current


def extended_dfs_path(visited, current):
    return current + visited


def main():
    graph = {
        'CDMX': ['MTY', 'PUE', 'JAL'],
        'MTY': ['CHH'],
        'CHH': ['SON'],
        'SON': ['SIN'],
        'PUE': ['MOR', 'HGO'],
        'HGO': ['VER', 'SIN'],
        'JAL': ['SIN'],
        'MOR': [],
        'VER': [],
        'SIN': []
    }

    bfs_path = bfs(graph, 'CDMX', 'HGO')
    dfs_path = dfs(graph, 'CDMX', 'HGO')

    print('bfs CDMX-HGO: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found'))
    print('dfs CDMX-HGO: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found'))

    tra_bfs_path = traverse(graph, 'CDMX', 'HGO', extended_bfs_path)
    print('template bfs CDMX-HGO: {}'.format(tra_bfs_path[1] if tra_bfs_path[0] else 'Not found'))

    tra_dfs_path = traverse(graph, 'CDMX', 'HGO', extended_dfs_path)
    print('template dfs CDMX-HGO: {}'.format(tra_dfs_path[1] if tra_dfs_path[0] else 'Not found'))


main()
