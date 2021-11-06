from typing import List, Dict, Set, Optional


class DoubleLinkedList:
    def __init__(self, value: int, prev_node: 'DoubleLinkedList' = None, next_node: 'DoubleLinkedList' = None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def add_next(self, next_node: 'DoubleLinkedList') -> None:
        self.next_node = next_node
        next_node.prev_node = self

    def add_prev(self, prev_node: 'DoubleLinkedList') -> None:
        self.prev_node = prev_node
        prev_node.next_node = self

    def remove_self(self):
        # doesn't actually delete me it just removes me from the chain idk how to do that in python
        if self.prev_node is not None:
            self.prev_node.next_node = self.next_node
        if self.next_node is not None:
            self.next_node.prev_node = self.prev_node

    def print_list(self) -> None:
        print(f"{self.value} -> ")
        if self.next_node is not None:
            self.next_node.print_list()


class LRUCache:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        # ideally this is a doubly linked list but oh well
        self.tasks_start: Optional[DoubleLinkedList] = None
        self.tasks_end: Optional[DoubleLinkedList] = None
        # maps ids to spots on the list
        self.task_map: Dict[int, DoubleLinkedList] = {}
        self.task_set: Set[int] = set()

    def remove_task(self, task: DoubleLinkedList) -> int:
        if task == self.tasks_start:
            self.tasks_start = task.next_node
        if task == self.tasks_end:
            self.tasks_end = task.prev_node
        task.remove_self()
        del self.task_map[task.value]
        self.task_set.remove(task.value)
        return task.value

    def hash_add(self, task: DoubleLinkedList) -> None:
        self.task_set.add(task.value)
        self.task_map[task.value] = task

    def add_to_front(self, task: DoubleLinkedList) -> None:
        task.next_node = self.tasks_start
        if self.tasks_start is not None:
            self.tasks_start.prev_node = task
        self.tasks_start = task
        self.hash_add(task)

    def add_new_task(self, task_value: int) -> None:
        task = DoubleLinkedList(task_value)
        if self.tasks_start is None:
            # is the first task
            self.tasks_end = task
            self.add_to_front(task)

        elif len(self.task_set) < self.max_size:
            if task.value in self.task_set:
                self.remove_task(self.task_map[task.value])
            self.add_to_front(task)

        else:
            if task.value in self.task_set:
                # don't evict, just move around
                self.remove_task(self.task_map[task.value])
                self.add_to_front(task)
            else:
                self.remove_task(self.tasks_end)
                self.add_to_front(task)


if __name__ == "__main__":
    tasks = range(5)
    max_tasks = 4
    cache = LRUCache(max_tasks)
    for task in tasks:
        cache.add_new_task(task)
        cache.tasks_start.print_list()
        print()
    cache.add_new_task(2)
    cache.tasks_start.print_list()
    print()
    cache.add_new_task(2)
    cache.tasks_start.print_list()
