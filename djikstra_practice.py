from collections import defaultdict, deque
from typing import List, Tuple
from queue import PriorityQueue


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(dict)

    def add_node(self, value: int) -> None:
        self.graph[value] = self.graph.get(value, {})

    def add_edge(self, a: int, b: int, weight: float) -> None:
        # only allows for one edge between nodes (also created nodes if they are in edges yikes)
        self.graph[a][b] = weight

    def add_nodes(self, nodes: List[int]) -> None:
        for node in nodes:
            self.add_node(node)

    def add_edges(self, edges: List[Tuple[int, int, float]]) -> None:
        for a, b, weight in edges:
            self.add_edge(a, b, weight)

    def construct_graph(self, nodes: List[int], edges: List[Tuple[int, int, float]]) -> 'Graph':
        self.add_nodes(nodes)
        self.add_edges(edges)
        return self

    def bfs(self, node: int) -> None:
        visited = set()
        q = deque()
        q.append(node)

        while len(q) > 0:
            node = q.popleft()

            if node not in visited:
                visited.add(node)
                print(node)
                for neighbour in self.graph[node].keys():
                    q.append(neighbour)

    def djikstra(self, source: int) -> Tuple[dict, dict]:
        dist, prev = {node: float('inf') for node in self.graph.keys()}, {node: None for node in self.graph.keys()}
        pq = PriorityQueue()
        pq.put((0, source))

        while pq.qsize() > 0:
            current_distance, node = pq.get()

            # there is already a shorter path
            if dist[node] < current_distance:
                continue

            for neighbour, additional_distance in self.graph[node].items():
                new_distance = current_distance + additional_distance
                if new_distance < dist[neighbour]:
                    prev[neighbour] = node
                    dist[neighbour] = new_distance
                    pq.put((new_distance, neighbour))

        return dist, prev

    def min_cost_a_b(self, a, b) -> float:
        dist, prev = self.djikstra(a)
        return dist[b]


if __name__ == "__main__":
    nodes = list(range(7))
    edges = [
        (0, 1, 0),
        (0, 2, 0),
        (1, 3, 1),
        (2, 3, 2),
        (3, 4, 3),
        (3, 5, 3),
        (2, 6, 2),
    ]

    graph = Graph().construct_graph(nodes, edges)
    graph.bfs(0)
    print(f"min cost from 0 -> 4: {graph.min_cost_a_b(0, 4)}")
