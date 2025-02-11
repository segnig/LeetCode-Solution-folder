class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_num = max(nums)
        min_num = min(nums)
        count_array = [0 for _ in range(min_num, max_num + 1)]

        for num in nums:
            count_array[num - min_num] += 1
        idx = 0
        for index in range(len(count_array)):
            while count_array[index] > 0:
                nums[idx] = index + min_num
                idx += 1
                count_array[index] -= 1
        return nums   