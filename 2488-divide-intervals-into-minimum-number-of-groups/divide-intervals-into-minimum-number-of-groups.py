class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        largest_bound = max([h for _, h in intervals])
        prefix_sum = [0] * (largest_bound + 3)

        for left, right in intervals:
            prefix_sum[left] += 1
            prefix_sum[right + 1] -= 1

        running_sum = 0
        for i in range(largest_bound):
            prefix_sum[i] += running_sum
            running_sum = prefix_sum[i]

        return max(prefix_sum)