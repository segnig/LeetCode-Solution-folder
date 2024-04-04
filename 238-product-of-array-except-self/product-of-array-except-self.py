class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pre_product = 1
        post_product = 1
        for i in range(len(nums)):
            result.append(pre_product)
            pre_product *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            result[i] *= post_product
            post_product *= nums[i]

        return result

        