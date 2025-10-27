class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dp(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]

            sentences = []

            for end in range(start+1, len(s)+1):
                word = s[start:end]

                if word in word_set:
                    for sub in dp(end):
                        sentences.append(word + (" " + sub if sub else ""))
            
            memo[start] = sentences
            return sentences

        result = dp(0)

        print(memo)

        return result
