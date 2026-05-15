class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        # Row wise validation
        i = 0
        while i < len(board):
            j = 0
            row_set = set()
            while j < len(board[i]):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in row_set:
                    return False
                else:
                    row_set.add(board[i][j])
                j += 1
            i += 1

        # Column Wise Validation
        i = 0
        columns = [set() for _ in range(9)]
        while i < len(board):
            j = 0
            while j < len(board[i]):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in columns[j]:
                    return False
                else:
                    columns[j].add(board[i][j])
                j += 1
            i += 1

        # Box Validation
        boxes = [set() for _ in range(9)]
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[i]):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                else:
                    boxes[(i // 3) * 3 + (j // 3)].add(board[i][j])
                j += 1
            i += 1

        return True
