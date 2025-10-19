class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        name_to_transactions = defaultdict(list)

        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time, amount = int(time), int(amount)

            name_to_transactions[name].append((time, amount, city, index))

        invalid_transactions = set()

        for name, transaction in name_to_transactions.items():
            transaction.sort()

            for i, tran in enumerate(transaction):
                time, amount, city, index = tran

                if amount > 1000:
                    invalid_transactions.add(index)
        
                
                for j in range(i+1, len(transaction)):
                    if city != transaction[j][2] and transaction[j][0] - time <= 60:
                        invalid_transactions.add(index)
                        invalid_transactions.add(transaction[j][-1])
                    elif transaction[j][0] - time > 60:
                        break
        
        result = []

        for i in range(len(transactions)):
            if i in invalid_transactions:
                result.append(transactions[i])

        return result