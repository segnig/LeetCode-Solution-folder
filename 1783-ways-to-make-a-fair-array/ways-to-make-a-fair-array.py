class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_indexies = [0]
        odd_indexies = [0]

        for index, num in enumerate(nums):
            if index % 2 == 0:
                even_indexies.append(even_indexies[-1] + num)
                odd_indexies.append(odd_indexies[-1])
            else:
                even_indexies.append(even_indexies[-1])
                odd_indexies.append(odd_indexies[-1] + num)

        result = 0

        for i in range(1, len(nums) + 1):
            odd = odd_indexies[i - 1] + even_indexies[-1] - even_indexies[i]
            even = even_indexies[i - 1] + odd_indexies[-1] - odd_indexies[i]
            if even == odd:
                result += 1

        return result