class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        timetaken = 0
        while True:
            for i in range(len(tickets)):
                if i == k and tickets[k] == 1:
                    return 1 + timetaken
                if tickets[i] > 0:
                    tickets[i] -= 1
                    timetaken += 1