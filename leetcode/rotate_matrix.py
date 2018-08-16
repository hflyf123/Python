# 给定一个 n × n 的二维矩阵表示一个图像。

# 将图像顺时针旋转 90 度。

# 说明：

# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range (i+1,length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(length):
            matrix[i] = matrix[i][::-1]


def main():
    matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    Su = Solution()
    print(Su.rotate(matrix))

if __name__ == '__main__':
    main()