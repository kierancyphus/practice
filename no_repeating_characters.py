from collections import Counter


class Solution:
    def __init__(self, string) -> None:
        self.string = string

    def is_non_repeating_substring_possible(self) -> bool:
        # the idea here is that as long as the sum of all the other letters is greater than or equal to
        # the letter frequency - 1, we can always put something in between
        frequencies = Counter(self.string)
        total = len(self.string)
        for letter, freq in frequencies.items():
            if not freq <= total - freq + 1:
                return False

        return True

    def get_non_repeating(self) -> str:
        frequencies = Counter(self.string)
        # get all letters in order of most frequency to least
        letters = sorted([(freq, word) for word, freq in frequencies.items()])[::-1]
        base_freq, base_letter = letters[0]
        letters = letters[1:]
        fillers = ["" for _ in range(base_freq)]

        for freq, letter in letters:
            for i in range(freq):
                fillers[i] += letter

        rval = ""
        for i in range(base_freq):
            rval += base_letter + fillers[i]

        return rval


if __name__ == "__main__":
    test = "aaabbcccc"
    solution = Solution(test)
    print(f"can rearrange: {solution.is_non_repeating_substring_possible()}")
    print(f"rearranged sequence: {test} -> {solution.get_non_repeating()}")
