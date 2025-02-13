class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window =defaultdict(int)

        for char in s2[:len(s1) -1]:
            window[char] += 1

        left = 0
        for right in range(len(s1) - 1, len(s2)):
            window[s2[right]] += 1
            if self.anagram(target, window):
                return True
            window[s2[left]] -= 1
            left += 1
        return False 
        

    def anagram(self, target, window):
        for char in target:
            if target[char] != window[char]:
                return False
        return True
        