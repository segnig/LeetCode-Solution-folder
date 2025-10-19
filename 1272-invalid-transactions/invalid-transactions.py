from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append([name, int(time), int(amount), city, t])
        
        result = set()
        
        for i in range(len(parsed)):
            name_i, time_i, amount_i, city_i, orig_i = parsed[i]
            
            if amount_i > 1000:
                result.add(orig_i + f"#{i}")
                continue

            for j in range(len(parsed)):
                if i == j:
                    continue
                    
                name_j, time_j, amount_j, city_j, orig_j = parsed[j]
                if name_i == name_j and city_i != city_j and abs(time_i - time_j) <= 60:
                    result.add(orig_i+f"#{i}")
                    result.add(orig_j+ f"#{j}")

        return list([res.split("#")[0]  for res in result])
