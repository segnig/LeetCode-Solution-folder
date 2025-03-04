class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L_counter, R_counter = 0, 0
        result = 0
        for char in s:
            L_counter += 1 if char == "L" else 0
            R_counter += 1 if char == "R" else 0
            if L_counter == R_counter:
                result += 1
        return result