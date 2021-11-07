from typing import Set, Optional, Dict
from collections import defaultdict


class StringSegmenter:
    def __init__(self, dictionary: Set[str], s: str) -> None:
        self.dictionary = dictionary
        self.s = s
        self.cache: defaultdict[str, Optional[bool]] = defaultdict(lambda: None)

    def can_segment_string(self, s: Optional[str] = None) -> bool:
        if s is None:
            s = self.s

        for i in range(len(s)):
            first, second = self.s[:i], self.s[i:]
            if first in self.dictionary:
                cached_value = self.cache[second]
                if cached_value is not None:
                    return cached_value

                if second in self.dictionary or len(second) == 0:
                    self.cache[second] = True
                    return True
                self.cache[second] = self.can_segment_string(second)
                return self.cache[second]
        return False


if __name__ == "__main__":
    dictionary = {"apple", "pie"}
    test_string = "applepie"
    segmenter = StringSegmenter(dictionary, test_string)

    print(f"Can split: {segmenter.can_segment_string()}")
