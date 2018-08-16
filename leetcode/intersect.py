# 给定两个数组，编写一个函数来计算它们的交集。
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lists = []
        for num in nums1:
            if num in nums2:
                lists.append(num)
                nums2.remove(num)
        return lists

def main():
    Su = Solution()
    print(Su.intersect([1,2,2,1], [2,2]))

if __name__ == '__main__':
    main()

# best anwser
# import collections
# class Solution:
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         return list((collections.Counter(nums1)&collections.Counter(nums2)).elements())