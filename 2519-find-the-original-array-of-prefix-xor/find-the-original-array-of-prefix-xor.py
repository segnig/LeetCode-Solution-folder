class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = []
        num = 0

        for _ in range(len(pref)):
            result.append(pref[_] ^ num)
            num = pref[_]

        return result
