class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        validBusinessLine = set(["electronics", "grocery", "pharmacy", "restaurant"])

        result = []

        for i in range(len(businessLine)):
            if self.codeValidator(code[i]) and isActive[i] and businessLine[i] in validBusinessLine:
                result.append(i)
        
        result.sort(key=lambda x: (businessLine[x], code[x]))

        return [code[i] for i in result]
        
    def codeValidator(self, code):
        if len(code) == 0:
            return False

        for char in code:
            if not ("a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9" or char == "_"):
                return False
        
        return True

