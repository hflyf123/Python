# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution:
    # my answer
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr = ''
        for i in digits:
            arr = arr + (str(i))
        num = int(arr)
        num += 1
        List = []
        for n in str(num):
            List.append(int(n))
        return List

    # best answer
    def plusOne_pro(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in digits:
            sum = sum * 10 + i
        return [int(x) for x in str(sum + 1)]


def main():
    arr = [1,2,3,9]
    s = Solution()
    print(s.plusOne(arr))
    
if __name__ == '__main__':
    main()



        
            
        