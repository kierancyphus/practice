from typing import Optional, List


class BinaryTree:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional['BinaryTree'] = None
        self.right: Optional['BinaryTree'] = None

    def add_left(self, left: 'BinaryTree'):
        self.left = left

    def add_right(self, right: 'BinaryTree'):
        self.right = right

    def print_tree(self, indent=""):
        print(indent + str(self.value))
        if self.left is not None:
            self.left.print_tree(indent + "\t")
        if self.right is not None:
            self.right.print_tree(indent + "\t")

    def mirror_tree(self) -> 'BinaryTree':
        # returns a copy of the mirrored tree
        copied_node = BinaryTree(self.value)
        if self.left is not None:
            copied_node.add_right(self.left.mirror_tree())
        if self.right is not None:
            copied_node.add_left(self.right.mirror_tree())
        return copied_node

    def find_all_paths(self, total: int, current: int = 0, results: List[str] = [], path: List[int] = []) -> List[str]:
        new_current = current + self.value

        if new_current == total:
            # current path works
            total_path = path + [self.value]
            results.append(" -> ".join(map(str, total_path)))

        if new_current <= total:
            if self.left is not None:
                self.left.find_all_paths(total, new_current, results, path + [self.value])
            if self.right is not None:
                self.right.find_all_paths(total, new_current, results, path + [self.value])

        return results


if __name__ == "__main__":
    nodes = [BinaryTree(value) for value in range(7)]
    nodes[0].add_right(nodes[2])
    nodes[0].add_left(nodes[1])
    nodes[1].add_right(nodes[4])
    nodes[1].add_left(nodes[3])
    nodes[2].add_right(nodes[6])
    nodes[2].add_left(nodes[5])
    # extra for the find all paths question
    nodes[3].add_left(BinaryTree(4))
    nodes[4].add_left(BinaryTree(4))
    nodes[4].add_right(BinaryTree(3))
    nodes[5].add_left(BinaryTree(2))
    nodes[5].add_right(BinaryTree(1))

    nodes[0].print_tree()
    mirrored = nodes[0].mirror_tree()
    print()
    mirrored.print_tree()

    print(nodes[0].find_all_paths(8))
