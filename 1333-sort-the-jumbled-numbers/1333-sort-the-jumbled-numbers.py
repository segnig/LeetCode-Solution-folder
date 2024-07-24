class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        result = []

        for h in range(len(nums)):
            num = nums[h]
            n = str(num) 
            n = [str(mapping[int(i)]) for i in n]
            n = int("".join(n))
            result.append((n, h, nums[h]))
        result.sort()
        result = [num[2] for num in result]
        return result
        