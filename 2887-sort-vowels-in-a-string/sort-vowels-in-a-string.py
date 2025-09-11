class Solution:
    def sortVowels(self, s: str) -> str:
        charWords = list(s)
        vowels = set(["a", "A", "E", "e", "i", "I", "o", "O", "u", "U"])
        vowel_indeies = []
        vowel_chars = []

        for index, char in enumerate(charWords):
            if char in vowels:
                vowel_indeies.append(index)
                vowel_chars.append(char)

        vowel_chars.sort()

        for i in range(len(vowel_chars)):
            charWords[vowel_indeies[i]] = vowel_chars[i]

        return "".join(charWords)