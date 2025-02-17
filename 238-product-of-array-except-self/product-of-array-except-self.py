class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1]
        post_product = [1]

        for i in range(len(nums)):
            pre_product.append(pre_product[i] * nums[i])
            post_product.append(post_product[-1] * nums[len(nums) - i - 1])

        post_product = post_product[::-1]
        result = []
        
        for i in range(1, len(nums) + 1):
            result.append(post_product[i] * pre_product[i - 1])  

        return result
        