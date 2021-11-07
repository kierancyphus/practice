from typing import Optional, List


class PalindromeFinder:
    def __init__(self, string: str):
        self.s = string
        self.cache: List[List[Optional[bool]]] = [[None for _ in range(len(string) + 1)] for _ in range(len(string) + 1)]

    def is_palindrome(self, s: Optional[str] = None, i: int = 0, j: int = 0) -> bool:
        if s is None:
            s = self.s

        # check cached value
        cached_value = self.cache[i][j]
        if cached_value is not None:
            return cached_value

        # base cases
        if len(s) == 0 or len(s) == 1 or (len(s) == 2 and s[0] == s[-1]):
            self.cache[i][j] = True
            return True

        # if endings match and inside is a palidrome
        if s[0] == s[-1]:
            self.cache[i][j] = self.is_palindrome(s[1:-1], i + 1, j - 1)
            return self.cache[i][j]
        # is not a palindrome
        else:
            self.cache[i][j] = False
            return False

    def find_all_palindrome_substrings(self) -> List[str]:
        palindromes: List[str] = []
        for i in range(len(self.s)):
            for j in range(i + 1, len(self.s) + 1):
                # has to be +1 since slicing isn't inclusive
                if j - i > 1 and self.is_palindrome(self.s[i: j], i, j):
                    palindromes.append(self.s[i:j])
        return palindromes


if __name__ == "__main__":
    palindrome = "aabbbaa"
    finder = PalindromeFinder(palindrome)
    # print(f"{palindrome} is a palindrome: {finder.is_palindrome()}")
    # print(f"All palindromes in: {palindrome}")
    palindromes = finder.find_all_palindrome_substrings()
    print(palindromes)
