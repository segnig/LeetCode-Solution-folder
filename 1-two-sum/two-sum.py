class Solution(object):
    def twoSum(self, nums, target):
        nums_index = []

        for i, n in enumerate(nums):
            nums_index.append((n, i))

        nums_index.sort()

        left = 0
        right = len(nums_index) - 1

        while left < right:
            if target == nums_index[left][0] + nums_index[right][0]:
                return [nums_index[left][1], nums_index[right][1]]
            elif target > nums_index[left][0] + nums_index[right][0]:
                left += 1
            else:
                right -= 1
        