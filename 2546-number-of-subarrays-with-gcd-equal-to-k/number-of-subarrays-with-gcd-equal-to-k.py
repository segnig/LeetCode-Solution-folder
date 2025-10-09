class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            gcf = nums[i]
            for j in range(i, len(nums)):
                gcf = gcd(gcf, nums[j])
                count += gcf == k
                if k > gcf:break
        
        return count