class Solution:  
    def minimumPushes(self, word: str) -> int: 
        char_count = Counter(word)  
          
        sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)  
        
        total_pushes = 0  
        
        for i, (char, count) in enumerate(sorted_char_count):  
            total_pushes += ((i + 8)// 8) * count  

        return total_pushes