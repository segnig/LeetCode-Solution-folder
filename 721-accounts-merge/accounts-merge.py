class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return False
        if self.size[parent_u] > self.size[parent_v]:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_accounts = {}

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_accounts:
                    uf.union(idx, email_accounts[email])
                else:
                    email_accounts[email] = idx

        
        email_groups = defaultdict(list)
        for email, index in email_accounts.items():
            parent = uf.find(index)
            email_groups[parent].append(email)


        result = []
        for index, emails in email_groups.items():
            name = accounts[index][0]
            result.append([name] + sorted(emails))

        return result
