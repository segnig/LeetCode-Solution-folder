class Solution:
    def lengthOfLongestSubstring(self, word: str) -> int:
        counter = defaultdict(int)
    
        left = 0
        result = 0
        
        for right in range(len(word)):
            while counter[word[right]] > 0:
                counter[word[left]] -= 1
                left += 1
            counter[word[right]] += 1
            result = max(result, right - left + 1)
        
        return result