class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_numbers = [0, 1, 1]
        if len(tribonacci_numbers) < 3:
            return tribonacci_numbers[n]
        for i in range(3, n+1):
            tribonacci_numbers.append(tribonacci_numbers[-1] + tribonacci_numbers[-2] + tribonacci_numbers[-3])
        return tribonacci_numbers[n]