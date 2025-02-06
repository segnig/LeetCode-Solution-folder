class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_tuples = defaultdict(int)
        result = 0

        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                product = nums[j] * nums[i]
                product_tuples[product] += 1

        for prod in product_tuples:
            if product_tuples[prod] >= 2:
                num_tuples = product_tuples[prod] - 1
                result +=  (product_tuples[prod] * num_tuples) * 4

        print(product_tuples)
        return result