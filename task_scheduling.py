from typing import List, Tuple
from collections import defaultdict, deque


class TaskScheduler:
    def __init__(self, tasks: List[int], prerequisites: List[Tuple[int, int]]) -> None:
        self.tasks = tasks
        self.prerequisites = prerequisites
        self.graph = defaultdict(list)

    def add_node(self, node: int) -> None:
        # use current value if already there
        self.graph[node] = self.graph.get(node, [])

    def add_nodes(self, nodes: List[int]) -> None:
        for node in nodes:
            self.add_node(node)

    def add_edge(self, a: int, b: int) -> None:
        self.graph[a].append(b)

    def add_edges(self, edges: List[Tuple[int, int]]) -> None:
        for a, b in edges:
            self.add_edge(a, b)

    def construct_graph(self) -> None:
        self.add_nodes(self.tasks)
        self.add_edges(self.prerequisites)

    def print_graph(self, source: int) -> None:
        # essentially a bfs - I am just using this to see if I created the graph properly
        # I will choose the source so that it prints out the whole graph
        visited, q = set(), deque()
        q.append((source, ""))

        while len(q) > 0:
            node, indent = q.popleft()
            if node not in visited:
                visited.add(node)
                print(indent + str(node))
                for neighbour in self.graph[node]:
                    q.append((neighbour, indent + "  "))

    def can_schedule_all_tasks(self) -> bool:
        self.construct_graph()
        # create a graph and see if there are any loops
        visited = set()

        # need to do bfs at each node since they can be disconnected
        for node in self.graph.keys():
            q = deque()
            if node not in visited:
                q.append(node)

            while len(q) > 0:
                node = q.popleft()
                if node in visited:
                    return False
                visited.add(node)
                for neighbour in self.graph[node]:
                    q.append(neighbour)

        return True


if __name__ == "__main__":
    nodes = list(range(6))
    edges = [
        (0, 1),
        (1, 2),
        (0, 3),
        (4, 5),
    ]

    task_scheduler = TaskScheduler(nodes, edges)
    print(f"can schedule all tasks: {task_scheduler.can_schedule_all_tasks()}")
