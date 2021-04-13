from queue import Queue
max = 100
v = None
e = None
visited = [False for i in range(max)]
path = [0 for i in range(max)]
graph = [[] for i in range(max)]

def BFS(s):
    for i in range(v):
        visited[i] = False
        path[i] = -1
    
    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u

def printPath(s, f):
    b = []
    if f == s:
        print(s)
        return
    if path[f] == 1:
        print('No Path')
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break

        for i in range(len(b)-1, -1, -1):
            print(b[i], end=' ')

if __name__ == '__main__':
    v, e = map(int, input().split())
    for i in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 0
    f = 5
    BFS(s)
    printPath(s, f)