from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check the colum and row
        # check the single [square]
        for item in board:
            if len(item) != len(set(item)):
                #return False
                print("---\n")
        for i in range(9):
            print(i)


sol = Solution()


board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sol.isValidSudoku(board)
