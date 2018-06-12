#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        eor = 0
        for x in nums:
            eor = eor ^ x
        return eor

    def singleNumber_pro(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2 - sum(nums)