class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        n = len(s)
        for x in range(2**n):
            result = ""
            count = n - 1

            while count >= 0:
                which_case = x % 2 == 1
                x //= 2
                if not "0" <= s[count] <= "9":
                    if which_case:
                        result += s[count].lower()
                    else:
                        result += s[count].upper()
                else:
                    result += s[count]
                count -= 1

            ans.add(result[::-1])
        
        return list(ans)
        