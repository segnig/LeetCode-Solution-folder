class Solution(object):
    def minimumRecolors(self, blocks, k):
        default = defaultdict(int)
        for i in range(k):
            default[blocks[i]] += 1
        answer = min(default["W"], k)
        left, right = 0, k

        while right < len(blocks):
            default[blocks[right]] += 1
            default[blocks[left]] -= 1
            answer = min(default["W"], answer)
            left, right = left +1, right + 1
            
        
        return answer