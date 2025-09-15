class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        brokenLetters = set(list(brokenLetters))

        count = 0

        for word in text.split():
            for char in word:
                if char in brokenLetters:
                    break
            else:
                count += 1
        
        return count