from typing import List


class ZeroMover:
    def __init__(self, array: List[int]) -> None:
        self.array = array

    def move_zeros(self) -> None:
        # modifies array in place
        offset = 0
        for reverse_index, item in enumerate(self.array[::-1]):
            index = len(self.array) - 1 - reverse_index
            self.array[index + offset] = item
            if item == 0:
                offset += 1
            if index < offset:
                self.array[index] = 0


if __name__ == "__main__":
    array = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    print(f"original array: {array}")
    mover = ZeroMover(array)
    mover.move_zeros()
    print(f"moved array: {mover.array}")