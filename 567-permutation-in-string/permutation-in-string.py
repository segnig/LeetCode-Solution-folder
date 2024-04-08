class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        for i in range(len(s1)):
            counter1[s1[i]] += 1
        for i in range(len(s1)-1):
            counter2[s2[i]] += 1
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            counter2[s2[right]] += 1
            if counter1 == counter2:
                return True
            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            left += 1
            right += 1
        
        return False