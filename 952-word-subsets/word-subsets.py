class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_count = defaultdict(int)
        for word in words2:
            w_count = Counter(word)
            for char in w_count:
                word2_count[char] = max(word2_count[char], w_count[char])

        result = []
        for word in words1:
            word_counter = Counter(word)
            for char in word2_count:
                if word_counter[char] < word2_count[char]:
                    break
            else:
                result.append(word)
                 

        return result

        