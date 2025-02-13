class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window =defaultdict(int)
        result = []

        for char in s[:len(p) -1]:
            window[char] += 1

        left = 0
        for right in range(len(p) - 1, len(s)):
            window[s[right]] += 1
            if self.anagram(target, window):
                result.append(left)
            window[s[left]] -= 1
            left += 1
        return result
        

    def anagram(self, target, window):
        for char in target:
            if target[char] != window[char]:
                return False
        return True