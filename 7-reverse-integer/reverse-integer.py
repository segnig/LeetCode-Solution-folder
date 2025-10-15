class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        
        result = 0
        x = abs(x)
        while x > 0:
            curr_digit = x % 10
            x //= 10
            if result > (2 ** 31 - 1) / 10 - curr_digit + 1:
                return 0
            result = result * 10 + curr_digit
        
        result = result if not is_negative else -1 * result
        
        return result 
        """
        
        1534236469
        9646324351
        
        964632435
        
        -2**31// 10, 2**31 -1 /10
        is_negative = x < 0
        
        result = 0
        
        while x > 0:
            curr_digit = x % 10
            x //= 10
            if 
            result = result * 10 + curr_digit
        
        result = result if not is_negative else - result
        
        return result 
        
        """