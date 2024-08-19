class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        a, b = num1.split('+')
        c, d = num2.split('+')
        b, d = b[:-1], d[:-1]
        ab = int(a) * int(c) - int(b) * int(d)
        cd = int(b) * int(c) + int(a) * int(d)
        return str(ab) + '+' + str(cd) + 'i'
        