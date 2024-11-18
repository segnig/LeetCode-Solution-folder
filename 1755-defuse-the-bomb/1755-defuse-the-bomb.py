class Solution(object):
    def decrypt(self, code, k):
        N = len(code)

        if k == 0:
            return [0] * N
        left = 1 if k > 0 else N + k
        right = left + abs(k)

        code = code * 2

        cur_result = sum(code[left:right])

        result = [cur_result]

        count = 1
        while count < N:
            cur_result -= code[left]
            cur_result += code[right]
            result.append(cur_result)
            left, right = left + 1, right + 1
            count += 1
        
        return result