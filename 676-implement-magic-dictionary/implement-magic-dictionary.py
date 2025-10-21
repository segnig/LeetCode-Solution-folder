class MagicDictionary:

    def __init__(self):
        self.store = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                temp = list(word)
                temp[i] = "*"
                self.store[word].add("".join(temp))
        

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            word = list(searchWord)
            word[i] = "*"
            find_word = "".join(word)

            for key in self.store:
                if key != searchWord:
                    if find_word in self.store[key]:
                        return True
        
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)