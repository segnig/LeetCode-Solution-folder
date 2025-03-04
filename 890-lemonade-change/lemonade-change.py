class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counters = {
            5: 0, 10: 0, 15: 0, 20: 0
        }
        for bill in bills:
            b = bill
            if bill == 20:
                if counters[10] > 0:
                    counters[10] -= 1
                    bill = 10
            if bill > 5:
                if (bill - 5) // 5 <= counters[5]:
                    counters[5] -= (bill - 5) // 5
                else:
                    return False
            counters[b] += 1
        return True