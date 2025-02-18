class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        copy_nums = []
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        store = {0:-1}
        result = 0

        for i in range(len(nums)):
            if nums[i] in store:
                result = max(result, i - store[nums[i]])
            else:
                store[nums[i]] = i

        print(store)
        return result