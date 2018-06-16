# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
class Solution:
    # my answer
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        time = 0
        for i in nums:
            if i == 0:
                time += 1
        for a in range(time):
            nums.remove(0)
            nums.append(0)
    
    # best answer
    def moveZeroes_pro(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = 0
        for i in range(0,l):
            if nums[i-k] == 0:
                del nums[i-k]
                nums.append(0)
                k = k+1

def main():
    nums = [0, 0, 1, 12]
    s = Solution()
    s.moveZeroes_pro(nums)
    print(nums)

if __name__ == '__main__':
    main()