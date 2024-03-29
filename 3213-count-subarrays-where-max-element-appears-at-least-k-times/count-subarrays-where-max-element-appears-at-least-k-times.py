class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx,ans,l,r,n=max(nums),0,0,0,len(nums)
        while r<n:
            if nums[r]==mx:
                k-= 1
            r +=  1
            while k == 0:
                if nums[l] == mx:
                    k += 1
                l+=1
            ans += l
        return ans