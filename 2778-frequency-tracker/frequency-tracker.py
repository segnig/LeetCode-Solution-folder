class FrequencyTracker(object):

    def __init__(self):
        # Data structure
        self.store = defaultdict(int)
        self.frequency = defaultdict(int)
        

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.store[number] > 0:
            self.frequency[self.store[number]] -= 1

        self.store[number] += 1
        self.frequency[self.store[number]] += 1
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.store[number] > 0:

            self.frequency[self.store[number]] -= 1
            self.store[number] -= 1

            if self.store[number] > 0:
                self.frequency[self.store[number]] += 1
            

        if self.store[number] == 0:
            del self.store[number]

        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return self.frequency[frequency] > 0
        
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)