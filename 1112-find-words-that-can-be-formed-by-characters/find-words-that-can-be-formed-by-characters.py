class Solution(object):
    def countCharacters(self, words, chars):

        chars_counter = defaultdict(int)
        for char in chars:
            chars_counter[char] += 1

        
        res = 0
        for word in words:
            if self.helper(word, chars_counter):
                res += len(word)
        
        return res
    

    def helper(self, word, chars_counter):
        word = Counter(word)

        for char in word:
            if word[char] > chars_counter[char]:
                return False
        return True