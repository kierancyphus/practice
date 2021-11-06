from collections import defaultdict
from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_node(self, value):
        # doesn't doubleadd or remove previous ones
        self.graph[value] = self.graph.get(value, {})

    def add_edge(self, a, b, value):
        self.graph[a][b] = value

    def dijkstra(self, source):
        prev, dist = {v: None for v in self.graph.keys()}, {v: float('inf') for v in self.graph.keys()}
        print(dist)
        pq = PriorityQueue()

        dist[source] = 0
        pq.put((0, source))

        while pq.qsize() > 0:
            current_distance, current_node = pq.get()

            if current_distance > dist[current_node]:
                continue

            for neighbour, weight in self.graph[current_node].items():
                new_distance = current_distance + weight
                if new_distance < dist[neighbour]:
                    dist[neighbour] = new_distance
                    prev[neighbour] = current_node
                    pq.put((new_distance, neighbour))

        return prev, dist

    def bfs_to_end(self, start, end):
        prev, dist = self.dijkstra(start)
        return dist[end]

    def backtrack(self, prev, a, b):
        path = []
        while b != a:
            path.append(b)
            b = prev[b]
        path.append(b)
        return path

    def shortest_route(self, a, b):
        prev, dist = self.dijkstra(a)
        route = self.backtrack(prev, a, b)
        return route[::-1]


if __name__ == "__main__":
    nodes = list(range(6))
    edges = [(0, 1), (0, 2), (2, 3), (1, 3), (3, 4), (3, 5)]
    graph = Graph()
    for node in nodes:
        graph.add_node(node)
    for a, b in edges:
        graph.add_edge(a, b, a)

    print(graph)
    graph.add_node(6)
    graph.add_edge(2, 6, 1)

    print(f"distance to 4: {graph.bfs_to_end(0, 4)}")
    print(f"shortest route to 4: {graph.shortest_route(0, 4)}")
