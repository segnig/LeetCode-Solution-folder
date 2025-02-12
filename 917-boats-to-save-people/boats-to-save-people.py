class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right, left = len(people) - 1, 0

        result = 0

        while left < right:
            if people[right] + people[left] > limit:
                result += 1
                right -= 1
            else:
                result += 1
                right -= 1
                left += 1
        if left == right:
            result += 1
        return result
