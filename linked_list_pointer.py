from typing import Union
from collections import deque


class WeirdListNode:
    def __init__(self, value: str) -> None:
        self.value: str = value
        self.next: Union[None, 'WeirdListNode'] = None
        self.other: Union[None, 'WeirdListNode'] = None

    def add_next(self, next: 'WeirdListNode') -> None:
        self.next = next

    def add_other(self, other: 'WeirdListNode') -> None:
        self.other = other

    def print_next(self) -> None:
        # prints all next until end of list is reached
        print(self.value)
        if self.next is not None:
            self.next.print_next()

    def bfs(self) -> None:
        visited = set()
        q = deque()
        q.append(self)

        while len(q) > 0:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                print(node.value)
                if node.next is not None:
                    q.append(node.next)
                if node.other is not None:
                    q.append(node.other)

    def copy_graph(self) -> 'WeirdListNode':
        # this is actually quite complicated

        visited = set()
        q = deque()
        q.append(self)

        rval = copy = WeirdListNode(self.value)

        while len(q) > 0:
            node = q.popleft()
            if node not in visited:
                visited.add(node)


if __name__ == "__main__":
    nodes = [WeirdListNode(str(num)) for num in range(6)]
    for i in range(len(nodes) - 1):
        nodes[i].add_next(nodes[i + 1])

    others = [1, 0, 4, 1, 2, 0]
    for index, node in enumerate(nodes):
        node.add_other(nodes[others[index]])

    # nodes[0].print_next()
    nodes[2].bfs()
