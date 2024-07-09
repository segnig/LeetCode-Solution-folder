class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time_used = customers[0][0]
        result = 0
        for avl, tkn in customers:
            time_used = time_used + tkn if time_used > avl else avl + tkn
            print(time_used - avl)
            result += time_used - avl if time_used > avl else 0
        return result / len(customers)

        