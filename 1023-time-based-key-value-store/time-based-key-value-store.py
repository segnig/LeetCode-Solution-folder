class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        nums =  self.store[key]
        left = 0
        right = len(nums) - 1
        res = ""
        while left <= right:
            mid = (left + right)// 2
            if timestamp >= nums[mid][0]:
                res = nums[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)