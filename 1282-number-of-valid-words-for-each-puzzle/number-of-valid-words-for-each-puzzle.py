class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        word_to_num = Counter()

        for word in words:
            res = 0
            for char in word:
                pos = ord(char) - ord("a")
                res = res | 1 << pos
            word_to_num[res] += 1

        def helper(puz, f):
            result = 0
            pos = ord(f) - ord("a")
            cur = puz

            while cur > 0:
                if cur & 1 << pos:
                    result += word_to_num[cur]
                res = cur 
                res -= 1
                
                temp = puz & res
                cur = puz & temp
            return result

        ans = []
        for puzzle in puzzles:
            res = 0
            for char in puzzle:
                pos = ord(char) - ord("a")
                res = res | 1 << pos
            ans.append(helper(res, puzzle[0]))
        
        return ans