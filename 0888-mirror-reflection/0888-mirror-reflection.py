class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a, b):  
            while b:  
                a, b = b, a % b  
            return abs(a)
        y = q
        x = p
        gcd = gcd(y, x)
        y //= gcd
        x //= gcd

        if y % 2 == 0:
            return 0
        else:
            if x % 2 == 1:
                return 1
            else:
                return 2