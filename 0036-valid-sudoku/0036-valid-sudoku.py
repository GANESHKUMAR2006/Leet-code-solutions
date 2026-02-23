class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val=='.':
                    continue
                size=(r//3)*3+(c//3)
                if val in row[r] or val in col[c] or val in box[size]:
                    return False
                row[r].add(val)
                col[c].add(val)
                box[size].add(val)
        return True