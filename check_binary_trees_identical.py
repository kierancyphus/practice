from typing import Optional


class BinaryTree:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional['BinaryTree'] = None
        self.right: Optional['BinaryTree'] = None

    def print_tree(self, indent: str = ""):
        print(indent + str(self.value))
        if self.right is not None:
            self.right.print_tree(indent + "\t")
        if self.left is not None:
            self.left.print_tree(indent + "\t")

    def check_noneness(self, other: 'BinaryTree', direction: str):
        if direction == "left":
            return (self.left is not None and other.left is None) or (self.left is None and other.left is not None)
        elif direction == "right":
            return (self.right is not None and other.right is None) or (self.right is None and other.right is not None)
        else:
            raise ValueError(f"Error: direction={direction} is not a valid direction for a binary tree.")

    def check_identical(self, other: 'BinaryTree') -> bool:
        if self.value != other.value:
            return False
        right, left = True, True

        # check right
        if self.check_noneness(other, "right"):
            return False
        if self.right is not None and other.right is not None:
            right = self.right.check_identical(other.right)

        # check left
        if self.check_noneness(other, "left"):
            return False
        if self.left is not None and other.left is not None:
            left = self.left.check_identical(other.left)

        return left and right


def create_tree() -> BinaryTree:
    nodes = [BinaryTree(i) for i in range(7)]
    left_connections = [(0, 1), (1, 3), (2, 5)]
    right_connections = [(0, 2), (2, 6), (1, 4)]
    for a, b, in left_connections:
        nodes[a].left = nodes[b]

    for a, b in right_connections:
        nodes[a].right = nodes[b]

    return nodes[0]


if __name__ == "__main__":
    original = create_tree()
    copy = create_tree()
    print(f"trees are identical: {original.check_identical(copy)}")
