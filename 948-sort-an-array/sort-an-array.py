class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide(0, len(nums) - 1, nums)
        

    def merge(self, left_arr, right_arr):
        sorted_arr = []
        left , right = 0, 0

        while left < len(left_arr) and right < len(right_arr):
            if left_arr[left] <= right_arr[right]:
                sorted_arr.append(left_arr[left])
                left += 1
            else:
                sorted_arr.append(right_arr[right])
                right += 1
        if left < len(left_arr):
            sorted_arr.extend(left_arr[left:])
        else:
            sorted_arr.extend(right_arr[right:])

        return sorted_arr
    def divide(self, left, right, nums):
        if left == right:
            return [nums[left]]

        mid = (right + left) // 2
        left_nums = self.divide(left, mid, nums)
        right_nums = self.divide(mid + 1, right, nums)

        return self.merge(left_nums, right_nums)