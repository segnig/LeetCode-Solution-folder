class Solution(object):
    def intToRoman(self, num):
        num_roman = {
            1: 'I', 4: 'IV', 5:'V', 9: 'IX', 10: 'X', 40:'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000:'M'
        }
        result = ""

        nums = [n for n in num_roman.keys()]
        nums.sort(reverse=True)

        for n in nums:
            if num // n:
                repeat, remain = divmod(num, n)
                result += num_roman[n] * repeat
                num = remain
            
        return result