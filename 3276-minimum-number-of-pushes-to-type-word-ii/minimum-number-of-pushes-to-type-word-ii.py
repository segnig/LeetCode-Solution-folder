class Solution:
    def minimumPushes(self, word: str) -> int:
        word_counter = Counter(word)
        word_counter = list(word_counter.items())
        word_counter.sort(key=lambda x: x[1], reverse=True)
        result = 0
        for i, count in enumerate(word_counter):
            result += count[1] * ((i // 8) + 1)

        return result