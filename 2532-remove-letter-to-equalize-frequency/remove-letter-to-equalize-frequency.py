class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = list(Counter(word).values())

        counter_freq = Counter(counter)

        if len(counter_freq) > 2:
            return False
        elif len(counter_freq) == 1:
            for num, count in counter_freq.items():
                if count == 1:
                    return True
                if num == 1:
                    return True
            return False
        
        for num, count in counter_freq.items():
            if num == 1 and count == 1:
                return True
            if num + 1 in counter_freq and counter_freq[num+1] == 1:
                return True
        
        return False