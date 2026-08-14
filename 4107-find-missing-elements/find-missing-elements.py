class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        hash_set = set(nums)
        min_num, max_num = min(nums), max(nums)

        answer = []

        for num in range(min_num, max_num + 1):
            if num not in hash_set:
                answer.append(num)

        return answer