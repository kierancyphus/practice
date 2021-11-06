from collections import defaultdict, deque
from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_node(self, value):
        # replace with value if not exists, otherwise do nothing
        self.graph[value] = self.graph.get(value, {})

    def add_edge(self, a, b, weight):
        # add from a to b (overwrite if already exists)
        self.graph[a][b] = weight

    def bfs(self, start):
        explored = set()
        q = deque()
        q.append(start)
        explored.add(start)
        print(start)

        while len(q) != 0:
            node = q.popleft()
            for edge in self.graph[node].keys():
                if edge not in explored:
                    print(edge)
                    q.append(edge)
                    explored.add(edge)

    def dijsktra(self, source):
        # returns distances for all nodes and previous
        visited = set()
        pq = PriorityQueue()
        dist = {node: 0 for node in self.graph.keys()}
        prev = {node: None for node in self.graph.keys()}

        for v in self.graph.keys():
            if v != source:
                dist[v] = float('inf')
            pq.put((dist[v], v))

        while not pq.empty():
            current_distance, node = pq.get()

            if current_distance > dist[node]:
                continue

            for neighbour, neighbour_distance in self.graph[node].items():
                new_distance = current_distance + neighbour_distance
                if new_distance < dist[neighbour]:
                    dist[neighbour] = new_distance
                    prev[neighbour] = node
                    pq.put((new_distance, neighbour))

        return dist, prev

    def bfs_to_end(self, start, end):
        dist, _ = self.dijsktra(start)
        return dist[end]

    def __str__(self):
        return str(self.graph)


if __name__ == "__main__":
    nodes = list(range(5))
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
