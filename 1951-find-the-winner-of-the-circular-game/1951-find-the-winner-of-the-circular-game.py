class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [j + 1 for j in range(n)]
        h = 0
        while len(friends) != 1:
            h = (h + k - 1) % n
            friends.remove(friends[h])
            n -= 1
        res = friends[0]
        return res
        