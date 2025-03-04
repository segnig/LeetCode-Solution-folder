class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles:
                target //= 2
                maxDoubles -= 1
                result += 1
            elif target % 2 == 1 and maxDoubles:
                target -= 1
                result += 1
            else:
                return result + target - 1
        return result