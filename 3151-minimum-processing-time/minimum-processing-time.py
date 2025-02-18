class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        result = float("-inf")

        for i in range(0, len(tasks), 4):
            result = max(tasks[i+3] + processorTime[i//4], result)

        return result