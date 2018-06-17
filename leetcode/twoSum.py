# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


class Solution:
    # my answer
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            v = target - nums[i]
            if v in nums:
                if i != nums.index(v):
                    return i, nums.index(v)
                else:
                    continue
    
    # best answer
    def twoSum_pro(self, nums, target):
        n = len(nums)
        hash = {}
        for i in range(n):
            complement = target - nums[i]
            if hash.__contains__(complement):
                return [hash[complement], i]
            hash[nums[i]] = i
        raise Exception("No match pair")

def main():
    nums = [1,2,7,9]
    target = 9
    s = Solution()
    print(s.twoSum_pro(nums, target))

if __name__ == '__main__':
    main()
