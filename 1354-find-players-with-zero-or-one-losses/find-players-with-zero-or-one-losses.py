
class Solution(object):
    def findWinners(self, matches):
        losers_ones = defaultdict(int)
        winners = set()
        for winner, loser in matches:
            losers_ones[loser] += 1
            winners.add(winner)

        wins = [player for player in winners if player not in losers_ones]
        loses_ones = [player for player in losers_ones if losers_ones[player] == 1]
        wins.sort()
        loses_ones.sort()
        return [wins, loses_ones]

        