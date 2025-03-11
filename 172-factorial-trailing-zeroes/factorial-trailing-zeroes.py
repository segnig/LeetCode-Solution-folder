class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(100000)
        result = 0
        word = str(self.factorial(n))[::-1]
        for char in word:
            if char == "0":
                result += 1
            else:
                break
        return result


    def factorial(self, n):
        res = 1
        for i in range(n, 0, -1):
            res *= i
        return res
