# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 我的答案
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            a = nums.pop()
            nums.insert(0, a)
        return nums
# 最快答案
    def rotate_pro(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = k % length
        nums[:] = nums[-i:]+nums[:-i]
# a = Solution()
# nums = [1,2,3,4,5,6,7]
# k = 3
# print(a.rotate(nums, k))
#