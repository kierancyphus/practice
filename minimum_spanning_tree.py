from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, deque
from queue import PriorityQueue


class Graph:
    def __init__(self):
        # this is a fully connected, weighted graph
        self.graph: defaultdict[int, Dict[int, int]] = defaultdict(dict)

    def add_node(self, node: int) -> None:
        # doesn't override existing nodes
        self.graph[node] = self.graph.get(node, {})

    def add_nodes(self, nodes: List[int]) -> None:
        for node in nodes:
            self.add_node(node)

    def add_edge(self, a: int, b: int, weight: int) -> None:
        # this is an undirected graph
        self.graph[a][b] = weight
        self.graph[b][a] = weight

    def add_edges(self, edges: List[Tuple[int, int, int]]) -> None:
        for a, b, weight in edges:
            self.add_edge(a, b, weight)

    def construct_graph(self, nodes: List[int], edges: List[Tuple[int, int, int]]) -> 'Graph':
        self.add_nodes(nodes)
        self.add_edges(edges)
        return self

    def print_bfs(self, node: int, indent: str = "") -> None:
        visited, q = set(), deque()
        q.append(node)

        while len(q) > 0:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                print(indent + str(node))
                for neighbour in self.graph[node].keys():
                    q.append(neighbour)

    def get_minimum_spanning_tree(self) -> 'Graph':
        # I'm just going to reuse the graph class because a tree is technically a graph
        visited: Set[int] = set()
        pq: PriorityQueue[Tuple[int, int, Optional[int]]] = PriorityQueue()
        initial_node = list(self.graph.keys())[0]
        pq.put((0, initial_node, None))
        spanning_tree = Graph()
        while pq.qsize() > 0:
            distance, node, parent_node = pq.get()
            if node not in visited:
                visited.add(node)
                spanning_tree.add_node(node)
                if parent_node is not None:
                    spanning_tree.add_edge(node, parent_node, distance)
                for neighbour, distance in self.graph[node].items():
                    pq.put((distance, neighbour, node))

        return spanning_tree


if __name__ == "__main__":
    nodes = list(range(5))
    edges = [
        (0, 1, 2),
        (1, 2, 1),
        (0, 2, 4),
        (2, 3, 1),
        (0, 3, 5),
        (0, 4, 6),
        (3, 4, 9),
    ]

    graph = Graph().construct_graph(nodes, edges)
    # graph.print_bfs(0)
    # print(graph.graph)
    spanning_tree = graph.get_minimum_spanning_tree()
    spanning_tree.print_bfs(0)
    print(spanning_tree.graph)
