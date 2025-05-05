class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = [(task[0], task[1], index) for index , task in enumerate(tasks)]
        tasks.sort()

        order = []
        queue = []

        time = tasks[0][0]
        index = 0

        while index < len(tasks):
            if time < tasks[index][0]:
                time = tasks[index][0]
            while  index < len(tasks) and tasks[index][0] <= time:
                heappush(queue, tasks[index][1:])
                index += 1
            while index < len(tasks) and  time < tasks[index][0] and queue:
                time_take, idx = heappop(queue)
                time += time_take
                order.append(idx)

        while queue:
            time_take, idx = heappop(queue)
            order.append(idx)
        
        return order