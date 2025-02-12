class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        placeholder = 0
        seeker = 0

        while seeker < len(nums) and placeholder < len(nums):
            if nums[placeholder] == 0:
                while seeker < len(nums) and nums[seeker] == 0:
                    seeker += 1 

                if seeker < len(nums):
                    nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
                    placeholder, seeker = placeholder + 1, seeker + 1
    
            else:
                placeholder, seeker = placeholder + 1, seeker + 1



        return nums     