class Solution(object):
    def findWords(self, words):

        result = []
        for word in words:
            if self.helper(word):
                result.append(word)
        
        return result



    def helper(self, word):
        row_1 = set("qwertyuiop")
        row_2 = set("asdfghjkl")
        row_3 = set("zxcvbnm")

        word = set(word.lower())

        return (len(row_1) == len(word.union(row_1)) 
        or len(row_2) == len(word.union(row_2)) or len(row_3) == len(word.union(row_3)))

        