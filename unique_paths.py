# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def __init__(self, board):
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.start, self.num_free = self.setup()

    def setup(self):
        start = None
        num_blocked = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    start = (i, j)
                elif self.board[i][j] == -1:
                    num_blocked += 1
        return start, self.m * self.n - num_blocked

    def get_moves(self, position, visited):
        i, j = position
        moves = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1),
        ]

        # filter for board boundaries and full squares
        moves = [(i, j) for i, j in moves if 0 <= i < self.m and 0 <= j < self.n and self.board[i][j] != -1]

        # filter for visits
        return [move for move in moves if move not in visited]

    def unique_paths_helper(self, start, visited):
        i, j = start
        if self.board[i][j] == 2 and len(visited) == self.num_free:
            return 1
        total = 0
        for move in self.get_moves(start, visited):
            # backtrack
            visited.add(move)
            total += self.unique_paths_helper(move, visited)
            visited.remove(move)
        return total

    def unique_paths(self):
        # need to find start square
        visited = {self.start}
        return self.unique_paths_helper(self.start, visited)


if __name__ == "__main__":
    test_case = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    solution = Solution(test_case)
    print(f"Number of unique paths that pass over all 0 squares: {solution.unique_paths()}")
