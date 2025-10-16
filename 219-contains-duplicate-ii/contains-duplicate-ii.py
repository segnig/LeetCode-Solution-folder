class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def deafult():
            return -100002

        last_indeies = defaultdict(deafult)

        for i in range(len(nums)):
            if last_indeies[nums[i]] + k >= i:
                return True
            last_indeies[nums[i]] = i
        
        return False