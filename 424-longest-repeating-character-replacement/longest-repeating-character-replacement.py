class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        left = 0
        most_similar = 0
        result = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            most_similar = max(most_similar, counter[s[right]])

            while (right - left + 1) - most_similar > k:
                counter[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result