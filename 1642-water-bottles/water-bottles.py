class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            result += (numBottles // numExchange)
            numBottles = numBottles % numExchange + numBottles // numExchange
        return result
        