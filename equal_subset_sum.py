from typing import List, Optional
from math import ceil


class Solution:
    def __init__(self, numbers: List[int]) -> None:
        # Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements
        # in both subsets is equal.
        self.numbers: List[int] = numbers
        self.total: int = 0
        for number in self.numbers:
            self.total += number
        # this question in the same as is there some subset of numbers that equals half the total
        self.goal: float = self.total / 2
        self.cache: List[List[Optional[bool]]] = [[None for _ in range(ceil(self.goal) + 1)] for _ in range(len(numbers) + 1)]

    def solve(self, accum: int = 0, number_index: int = 0) -> int:
        if number_index == len(self.numbers):
            # ran out of numbers
            self.cache[number_index][accum] = False
            return False

        # check for cached value
        cached_value = self.cache[number_index][accum]
        if cached_value is not None:
            return cached_value

        new_accum: int = accum + self.numbers[number_index]
        if new_accum == self.goal:
            self.cache[number_index][accum] = True
            return True

        if new_accum > self.goal:
            # goes over the limit, so we skip adding this number
            self.cache[number_index][accum] = self.solve(accum, number_index + 1)
            return self.cache[number_index][accum]
        else:
            # solution either contains number or doesn't (the or of them)
            self.cache[number_index][accum] = self.solve(accum, number_index + 1) or self.solve(new_accum, number_index + 1)
            return self.cache[number_index][accum]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    solution = Solution(numbers)
    print(f"Can separate numbers equally: {solution.solve()}")

