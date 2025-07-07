class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for num in counter:
            if counter[num] == 2:
                result.append(num)

        return result