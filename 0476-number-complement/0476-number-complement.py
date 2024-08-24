class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_bi = ""

        while num:
            num_bi += str(num%2)
            num //=2
        com = ""
        for b in num_bi:
            com += "1" if b =="0" else "0"
        result = 0
        for i in range(len(com)):
            if com[i] == "1":
                result += 2**i
        return result