class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                box = (r // 3) * 3 + (c // 3)
                if num in row[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in grid[box]:
                    return False
                row[r].add(num)
                cols[c].add(num)
                grid[box].add(num)
        return True