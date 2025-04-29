class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if not self.small:
            heappush(self.small, -num)
        elif len(self.small) == len(self.large):
            heappush(self.large, num)
            popped_num = heappop(self.large)
            heappush(self.small, -popped_num)
            

        else:
            heappush(self.small, -num)
            popped_num = - heappop(self.small)
            heappush(self.large, popped_num)


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (- self.small[0] + self.large[0]) / 2
        return - self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()