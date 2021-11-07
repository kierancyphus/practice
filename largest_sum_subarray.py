from typing import List, Tuple


class LargestSumFinder:
    def __init__(self, array: List[int]) -> None:
        self.array = array

    def find_largest_value(self) -> int:
        # this is Kadane's algo
        if len(self.array) == 1:
            return self.array[0]

        # returns max value, (i, j)
        current_max = global_max = self.array[0]
        for number in self.array:
            current_max = max(number, current_max + number)
            if current_max > global_max:
                global_max = current_max

        return global_max


if __name__ == "__main__":
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    finder = LargestSumFinder(numbers)
    print(f"largest sum: {finder.find_largest_value()}")


