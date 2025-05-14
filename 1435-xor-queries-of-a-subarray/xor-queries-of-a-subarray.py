class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_XOR = [0]

        for num in arr:
            pre_XOR.append(pre_XOR[-1] ^ num)
        
        result = []

        for left, right in queries:
            result.append(
                pre_XOR[left] ^ pre_XOR[right+1]
            )
        return result
        