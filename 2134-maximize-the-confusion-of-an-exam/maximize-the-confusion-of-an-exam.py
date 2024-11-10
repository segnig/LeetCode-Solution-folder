class Solution(object):  
    def maxConsecutiveAnswers(self, answerKey, k):  
        
        left = 0

        count = 0
        res = 0

        for i in range(len(answerKey)):
            if answerKey[i] == "T":
                count += 1

            while count > k:
                if answerKey[left] == "T":
                    count -= 1
                left += 1
            res = max(res, i - left + 1)

        left = 0

        count = 0

        for i in range(len(answerKey)):
            if answerKey[i] != "T":
                count += 1

            while count > k:
                if answerKey[left] != "T":
                    count -= 1
                left += 1
            res = max(res, i - left + 1)
        return res