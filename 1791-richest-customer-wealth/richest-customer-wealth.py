class Solution(object):
    def maximumWealth(self, accounts):
        total_wealths = [sum(account) for account in accounts]
        return max(total_wealths)
        