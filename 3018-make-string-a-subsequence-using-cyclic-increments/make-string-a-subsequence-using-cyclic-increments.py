class Solution(object):  
    def canMakeSubsequence(self, str1, str2):  
        if len(str1) < len(str2):
            return False
        def match(x):      
            return chr(ord("a") + (ord(x) - ord("a")  + 1) % 26) 

        p1 = 0 
        for x in range(len(str2)):  
            while p1 < len(str1) and not (str1[p1] == str2[x] or match(str1[p1]) == str2[x]):  
                p1 += 1
            
            if p1 < len(str1) and x == len(str2) - 1:
                return True
            if p1 < len(str1):
                p1 += 1
        return False 