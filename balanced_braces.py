from collections import defaultdict, deque


class BraceBalancer:
    def __init__(self, n: int, left_brackets="{", right_brackets="}"):
        # n is number of braces (assumed to be even)
        # also assuming there is only one type of brace
        self.n = n
        if n % 2 != 0:
            raise ValueError("Error: n has to be an even number")
        self.left_brackets = left_brackets
        self.right_brackets = right_brackets
        self.bracket_counter = defaultdict(int)
        self.pairs = list(zip(left_brackets, right_brackets))

        # this is a set that keeps track of all balanced pairs
        self.balanced = set(self.pairs)

        # used for determining if we can open and close things
        self.open_q = deque()

    def get_braces(self, accum="", left=0, right=0):
        if left + right == self.n:
            if left == right:
                # proper matching
                print(accum)
                return
        elif left > self.n / 2 or right > self.n / 2:
            # there is no way to balance the braces
            return
        else:
            # can add a left or a right bracket
            self.get_braces(accum + "{", left + 1, right)
            # can only add right if there is already one on the left
            if left > right:
                self.get_braces(accum + "}", left, right + 1)

    def is_balanced(self, left, right):
        return self.bracket_counter[left] == self.bracket_counter[right]

    def get_multiple_braces(self, accum=""):
        if len(accum) == self.n:
            if len(self.balanced) == len(self.left_brackets):
                # proper matching
                print(accum)
        else:
            for left, right in self.pairs:
                # can add left on any open, can only close on same open. When adding right, set the open as prev

                # add left: update counter and remove from balanced
                self.bracket_counter[left] += 1
                if (left, right) in self.balanced:
                    self.balanced.remove((left, right))
                # add left: update open
                self.open_q.append(left)
                self.get_multiple_braces(accum + left)
                self.open_q.pop()
                self.bracket_counter[left] -= 1

                # check for balance
                if self.is_balanced(left, right):
                    self.balanced.add((left, right))

                # add right if there is room
                if self.bracket_counter[left] > self.bracket_counter[right] and self.open_q[-1] == left:
                    self.bracket_counter[right] += 1
                    if self.is_balanced(left, right):
                        # we can balance by adding rights, so have to check
                        self.balanced.add((left, right))

                    # need to pop one off the queue
                    temp = self.open_q.pop()
                    self.get_multiple_braces(accum + right)
                    self.open_q.append(temp)

                    self.bracket_counter[right] -= 1
                    if self.is_balanced(left, right):
                        # can also unbalance by removing, so have to check again
                        self.balanced.add((left, right))


if __name__ == "__main__":
    balancer = BraceBalancer(6, "{([", "})]")
    balancer.get_braces()
    print()
    balancer.get_multiple_braces()

