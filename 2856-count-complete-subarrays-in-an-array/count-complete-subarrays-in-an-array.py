class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        number_of_completed_subarray = 0
        left = 0
        num_of_distinict_number = len(set(nums))
        element_counter = Counter()

        for right in range(len(nums)):
            element_counter[nums[right]] += 1

            while len(element_counter) == num_of_distinict_number:
                number_of_completed_subarray += len(nums) - right
                element_counter[nums[left]] -= 1

                if element_counter[nums[left]] == 0:
                    del element_counter[nums[left]]
                left += 1

        return number_of_completed_subarray