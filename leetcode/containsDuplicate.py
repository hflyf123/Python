# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
class Solution:
    # my answer
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != len(set(nums)):
            return True
        else:
            return False

    # best answer
    def containsDuplicate_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        else:
            return True