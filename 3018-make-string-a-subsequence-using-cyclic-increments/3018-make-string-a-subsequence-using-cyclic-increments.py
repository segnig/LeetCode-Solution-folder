class Solution(object):  
    def canMakeSubsequence(self, str1, str2):  
        if len(str1) < len(str2):
            return False
        def match(x):   
            a = ord("a") 
            x = ord(x)  
            dif = x - a + 1
            res = chr(a + dif % 26)  
            return res

        p1 = 0 
        
        
        for x in range(len(str2)):  
            while p1 < len(str1) and not (str1[p1] == str2[x] or match(str1[p1]) == str2[x]):  
                p1 += 1
            
            if p1 < len(str1) and x == len(str2) - 1:
                return True
            if p1 < len(str1):
                p1 += 1
        return False 