class Solution:
    def numRabbits(self, answers):
        counter = Counter(answers) 
        result = 0
        for count in counter:
           group = ceil(counter[count] / (count + 1))
           result += group * (count + 1)
        return result