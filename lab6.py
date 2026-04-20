import heapq

def solve_gamsrv (start_node, n, graph):
    dist = [float('inf')] * (n + 1)
    dist[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))

    return dist

f_in = open("gamsrv.in", "r")
lines = f_in.readlines()
f_in.close()

n, m = map(int, lines[0].split())
clients = list(map(int, lines[1].split()))

graph = []
for i in range(n + 1):
    graph.append([])

for i in range(2, 2 + m):
    u, v, w = map(int, lines[i].split())
    graph[u].append((v, w))
    graph[v].append((u, w))

candidates = []
for i in range(1, n + 1):
    if i not in clients:
        candidates.append(i)

if len(candidates) == 0:
    result = 0
else:
    max_delays = {}
    for cand in candidates:
        max_delays[cand] = 0

    for client in clients:
        distances = solve_gamsrv(client, n, graph)

        for cand in candidates:
            if distances[cand] > max_delays[cand]:
                max_delays[cand] = distances[cand]

    result = float('inf')
    for cand in candidates:
        if max_delays[cand] < result:
            result = max_delays[cand]

f_out = open("gamsrv.out", "w")
f_out.write(str(result) + "\n")
f_out.close()