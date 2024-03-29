class Solution:
    def compress(self, chars: List[str]) -> int:
        result = [chars[0]]
        res = 1
        for i in range(1, len(chars)):
            if result[-1] != chars[i]:
                if res > 1:
                    result.append(str(res))
                result.append(chars[i])
                res = 1
            else:
                res += 1

        if res > 1:
            result.append(str(res))

        result = "".join(result)
        result = list(result)
        
        for i in range(len(result)):
            chars[i] = result[i]

       
        return len(result)
        

        