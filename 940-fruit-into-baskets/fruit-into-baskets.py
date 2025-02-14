class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = defaultdict(int)
        ans = 1
        left = 0
        for right in range(len(fruits)):
            while len(result) == 2 and fruits[right] not in result:
                result[fruits[left]] -= 1
                if result[fruits[left]] == 0:
                    del result[fruits[left]]
                ans = max(ans, right - left)
                left += 1
            result[fruits[right]] += 1
            ans = max(ans, right - left + 1)
        return ans