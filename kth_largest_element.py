from queue import PriorityQueue


class Solution:
    def __init__(self, array, k):
        self.array = array
        self.k = k
        self.window = PriorityQueue()
        # answer will be a sorted list that is populated after getting the kth largest element
        self.answer = []

    def get_kth_largest_element(self):
        # O(nlog(k))
        for index, value in enumerate(self.array):
            if index < 3:
                self.window.put(value)
            else:
                kth_value = self.window.get()
                self.window.put(max(value, kth_value))

        while self.window.qsize() > 0:
            self.answer.append(self.window.get())
        return self.answer[0]

    def add(self, value):
        # O(1)
        self.array.append(value)
        if value > self.answer[0]:
            return min(value, self.answer[1])
        return self.answer[0]


if __name__ == "__main__":
    test = [1, 23, 56, 76, 31, 21, 4, 6]
    k = 3
    solution = Solution(test, k)

    print(f"{k}th largest value: {solution.get_kth_largest_element()}")
    a = 100
    print(f"adding: {a}. {k}th largest value: {solution.add(a)}")

