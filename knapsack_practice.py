from typing import List


class Knapsack:
    def __init__(self, values: List[int], weights: List[int], capacity: int) -> None:
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.n = len(weights)
        self.cache = [[-1 for _ in range(capacity + 1)] for _ in range(self.n)]
        self.iterate_cache = [[0 for _ in range(capacity + 1)] for _ in range(self.n)]

    def solve_recursion(self, n=None, capacity=None):
        if n is None:
            n = self.n - 1
        if capacity is None:
            capacity = self.capacity

        if n == 0 or capacity == 0:
            return 0

        cached_value = self.cache[n][capacity]
        if cached_value != -1:
            return cached_value

        if self.weights[n] > capacity:
            # can't add
            self.cache[n][capacity] = self.solve_recursion(n - 1, capacity)
            return self.cache[n][capacity]

        else:
            # one of the two
            self.cache[n][capacity] = max(
                self.solve_recursion(n - 1, capacity),
                self.values[n] + self.solve_recursion(n - 1, capacity - self.weights[n])
            )
            return self.cache[n][capacity]

    def solve_iteratively(self) -> int:
        for item in range(self.n):
            for capacity in range(self.capacity + 1):
                if capacity == 0:
                    continue

                elif item == 0:
                    # if we can only have the first item, then we always choose it
                    self.iterate_cache[item][capacity] = self.values[item]

                elif self.weights[item] > capacity:
                    # don't have space to add the new one, choose the previous capacity value
                    self.iterate_cache[item][capacity] = max(
                        self.iterate_cache[item][capacity - 1],
                        self.iterate_cache[item - 1][capacity]
                    )

                else:
                    # will the max of including it or not
                    self.iterate_cache[item][capacity] = max(
                        self.iterate_cache[item - 1][capacity],
                        self.values[item] + self.iterate_cache[item - 1][capacity - self.weights[item]]
                    )

        return self.iterate_cache[-1][-1]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    knapsack = Knapsack(values, weights, capacity)
    print(f"optimal value: {knapsack.solve_recursion()}")

    print(f"optimal value (iterative): {knapsack.solve_iteratively()}")
