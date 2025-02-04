class Solution(object):
    def getSneakyNumbers(self, nums):
        counter = Counter(nums)
        result = []

        for num in counter:
            if counter[num] > 1:
                result.append(num)
        
        return result