class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        sum_of_digits = sum([int(digit) for digit in str(n)])
        prod_of_digits = 1

        for digit in str(n):
            prod_of_digits *= int(digit)

        return n % (sum_of_digits + prod_of_digits) == 0