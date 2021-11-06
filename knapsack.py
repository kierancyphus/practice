from typing import Optional, List


class Knapsack01:
    def __init__(self, values, weights, capacity):
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.cache = [[-1 for _ in range(len(weights) + 1)] for _ in range(capacity + 1)]

    def solve(self, n: Optional[int] = None, capacity: Optional[int] = None) -> int:
        if capacity is None:
            capacity = self.capacity
        if n is None:
            n = len(self.values)

        cached_value = self.cache[capacity][n]
        if cached_value != -1:
            return cached_value

        if n == 0 or capacity == 0:
            return 0

        if self.weights[n - 1] > capacity:
            self.cache[capacity][n] = self.solve(n - 1, capacity)
            return self.cache[capacity][n]

        else:
            self.cache[capacity][n] = max(
                self.solve(n - 1, capacity),
                self.values[n - 1] + self.solve(n - 1, capacity - self.weights[n - 1])
            )
            return self.cache[capacity][n]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    solution = Knapsack01(values, weights, capacity)
    print(f"best value: {solution.solve()}")
