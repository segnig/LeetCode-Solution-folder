class MagicDictionary:

    def __init__(self):
        self.store = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            length = len(word)
            self.store[length].append(word)

    def search(self, searchWord: str) -> bool:
        candidate_words = self.store[len(searchWord)]

        for candidate_word in candidate_words:
            change_needed = 0

            for i in range(len(searchWord)):
                if candidate_word[i] != searchWord[i]:change_needed += 1
        
            if change_needed == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)