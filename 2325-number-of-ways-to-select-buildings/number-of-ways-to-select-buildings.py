class Solution:
    def numberOfWays(self, s: str) -> int:
    
        right_zeros = s.count("0")
        right_ones = s.count("1")
        total = 0
        left_zeros = 0
        left_ones = 0
        
        for index in range(len(s)):
            if s[index] == "1":
                total += left_zeros * right_zeros
                right_ones, left_ones = right_ones - 1, left_ones + 1
            else:
                total += left_ones * right_ones
                left_zeros, right_zeros = left_zeros + 1, right_zeros - 1 

        return total