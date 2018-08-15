# 有效的数独

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 每行的元素以一个字典储存,key是数字,value统一为1
        # 每列的元素
        # 每个九宫格
        dic_row = [{},{},{},{},{},{},{},{},{}]
        dic_col = [{},{},{},{},{},{},{},{},{}]
        dic_box = [{},{},{},{},{},{},{},{},{}]
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == '.':
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3*(i//3)+(j//3)][num] = 1
                else:
                    return False
        return True



def main():
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

    So = Solution()
    print(So.isValidSudoku(board))

if __name__ == '__main__':
    main()