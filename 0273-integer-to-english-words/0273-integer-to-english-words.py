class Solution:  
    def numberToWords(self, num: int) -> str:  
        if num == 0:  
            return "Zero"  
        
        def one(num):  
            if num == 0: return ""  
            elif num == 1: return "One"  
            elif num == 2: return "Two"  
            elif num == 3: return "Three"  
            elif num == 4: return "Four"  
            elif num == 5: return "Five"  
            elif num == 6: return "Six"  
            elif num == 7: return "Seven"  
            elif num == 8: return "Eight"  
            elif num == 9: return "Nine"  
        
        def two_less_20(num):  
            if num == 10: return "Ten"  
            elif num == 11: return "Eleven"  
            elif num == 12: return "Twelve"  
            elif num == 13: return "Thirteen"  
            elif num == 14: return "Fourteen"  
            elif num == 15: return "Fifteen"  
            elif num == 16: return "Sixteen"  
            elif num == 17: return "Seventeen"  
            elif num == 18: return "Eighteen"  
            elif num == 19: return "Nineteen"  
        
        def ten(num):  
            if num == 0: return ""  
            elif num == 2: return "Twenty"  
            elif num == 3: return "Thirty"  
            elif num == 4: return "Forty"  
            elif num == 5: return "Fifty"  
            elif num == 6: return "Sixty"  
            elif num == 7: return "Seventy"  
            elif num == 8: return "Eighty"  
            elif num == 9: return "Ninety"  

        def helper(num):  
            if num == 0:  
                return ""  
            elif num < 10:  
                return one(num)  
            elif num < 20:  
                return two_less_20(num)  
            elif num < 100:  
                return ten(num // 10) + (" " + one(num % 10) if num % 10 != 0 else "")  
            elif num < 1000:  
                return one(num // 100) + " Hundred" + (" " + helper(num % 100) if num % 100 != 0 else "")  
            elif num < 10**6:  
                return helper(num // 1000) + " Thousand" + (" " + helper(num % 1000) if num % 1000 != 0 else "")  
            elif num < 10**9:  
                return helper(num // 10**6) + " Million" + (" " + helper(num % 10**6) if num % 10**6 != 0 else "")  
            else:  
                return helper(num // 10**9) + " Billion" + (" " + helper(num % 10**9) if num % 10**9 != 0 else "")  

        return helper(num).strip()