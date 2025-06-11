class Solution:
    def queryString(self, s: str, n: int) -> bool:

        possible_numbers = set()
        for i in range(len(s)):
            for j in range(i, i + 30):
                possible_numbers.add(int(s[i:j+1], 2))

        for num in range(1, n + 1):
            if num not in possible_numbers:
                return False
        
        return True