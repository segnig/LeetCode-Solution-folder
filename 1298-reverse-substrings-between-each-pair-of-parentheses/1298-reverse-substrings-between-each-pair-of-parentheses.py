class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        res = ""
        
        for i in range(n):
            if s[i] == ")":
                if stack:
                    h = stack.pop()
                    rev_str = s[h:i+1][::-1]  
                    s = s[:h] + rev_str + s[i+1:] 
                    
            elif s[i] == "(":
                stack.append(i)
            print(s)
        
        res = ""
        for k in s:
            if k != "(" and k != ")":
                res += k
            
        return res