class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remain = 1
        res = 1
        array = set()

        while remain % k:
            if remain % k in array:
                return -1
            array.add(remain%k)
            remain = remain*10 + 1 
            res +=1
        return res


        