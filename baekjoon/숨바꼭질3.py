import sys

import heapq
def dijkstra(start, end):
    distance = [float('inf')] * 100001
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        if node == end:
            return dist
        if distance[node] < dist:
            continue
        for next_node in [node - 1, node + 1, node * 2]:
            if 0 <= next_node <= 100000:
                cost = dist + 1
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))


if __name__ == '__main__':
    t = dijkstra(5, 17)
    print(t)