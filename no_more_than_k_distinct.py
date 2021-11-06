from collections import defaultdict


class Solution:
    def __init__(self, k: int, string: str) -> None:
        self.k = k
        self.string = string

    def find_substring(self) -> str:
        # this is essentially just sliding window
        window_counter, window_set = defaultdict(int), set()
        left, right = 0, 0
        max_string = ""
        current_string = ""

        for letter in self.string:
            # increment right index
            right += 1
            current_string += letter
            window_counter[letter] += 1
            window_set.add(letter)

            while len(window_set) > self.k:
                # we have too many unique -> move left pointer until we are fine
                window_counter[self.string[left]] -= 1
                if window_counter[self.string[left]] == 0:
                    window_set.remove(self.string[left])
                left += 1
                current_string = current_string[1:]

            if len(current_string) > len(max_string):
                max_string = current_string

        return max_string


if __name__ == "__main__":
    test_string = "ababcbaddab"
    k = 3
    solution = Solution(k, test_string)
    print(solution.find_substring())
