from typing import List, Tuple


class IntervalMerger:
    def __init__(self, intervals: List[Tuple[int, int]]) -> None:
        self.intervals = intervals
        self.start = float('inf')
        self.end = float('inf')

    def merge_intervals(self) -> List[Tuple[int, int]]:
        if len(self.intervals) == 0:
            return []

        merged = []
        self.start, self.end = self.intervals[0]
        for start, end in self.intervals[1:]:
            if start <= self.end:
                # we are in the same interval
                if end > self.end:
                    # we can extend this interval
                    self.end = end
                # otherwise do nothing
            else:
                # a new interval has been reached, so we should store results and move on
                merged.append((self.start, self.end))
                self.start, self.end = start, end
        # need to add the last one
        merged.append((self.start, self.end))
        return merged


if __name__ == "__main__":
    # intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    intervals = [(1, 4), (4, 5)]
    merger = IntervalMerger(intervals)
    print(f"merged intervals: {merger.merge_intervals()}")
