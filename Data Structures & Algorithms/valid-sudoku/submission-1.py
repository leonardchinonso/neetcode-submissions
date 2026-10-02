'''
Brute Force:
    Do what the question asks - check each column, row and 3x3 sub boxes for duplicates, return false if found
    Time:
        Rows: O(81) - nine rows for each row we check all nine values in worst case
        Cols: O(81) - same as above
        3x3: O(81) - nine boxes, for each box we check all nine values
    Space: O(9) - at every point we hold max of nine numbers in the seen hashmap
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        return self.valid_rows() and self.valid_cols() and self.valid_3x3()

    def valid_rows(self) -> bool:
        for row in self.board:
            seen = defaultdict(bool)
            for item in row:
                if item != '.' and seen[item]:
                    return False
                seen[item] = True
        return True

    def valid_cols(self) -> bool:
        for c in range(len(self.board[0])):
            seen = defaultdict(bool)
            for r in range(len(self.board)):
                if self.board[r][c] != '.' and seen[self.board[r][c]]:
                    return False
                seen[self.board[r][c]] = True
        return True


    def valid_3x3(self) -> bool:
        count, N = 0, len(self.board)
        r_start, r_end = 0, 3
        c_start, c_end = 0, 3

        while count < N:
            seen = defaultdict(bool)
            for r in range(r_start, r_end):
                for c in range(c_start, c_end):
                    if self.board[r][c] != '.' and seen[self.board[r][c]]:
                        return False
                    seen[self.board[r][c]] = True
            if r_end < N:
                r_start += 3
                r_end += 3
            else:
                c_start += 3
                c_end += 3
                r_start = 0
                r_end = 3
            count += 1
        
        return True

'''
[
[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]
]
'''