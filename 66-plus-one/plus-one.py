class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits

        remain = 1
        index = len(digits) - 1
        while remain > 0:
            sum = digits[index] + remain
            digits[index] = sum % 10
            remain = sum // 10

            index -= 1
        
        return digits if digits[0] != 0 else digits[1:]