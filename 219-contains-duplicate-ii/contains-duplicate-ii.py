class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_indeies = {}

        for i in range(len(nums)):
            if nums[i] in last_indeies:
                if last_indeies[nums[i]] + k >= i:
                    return True
            last_indeies[nums[i]] = i
        
        return False