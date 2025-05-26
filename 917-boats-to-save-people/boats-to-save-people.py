class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r, l = len(people) - 1, 0

        ans = 0
        while l < r:
            if people[r] + people[l] > limit:
                ans += 1
                r -= 1
            else:
                ans += 1
                r -= 1
                l += 1
        if l == r:
            ans += 1
        return ans
