class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_characters = set(string.ascii_letters + string.digits)
        res = ""
        for n in s:
            if n in alphanumeric_characters:
                res += n
        left, right = 0, len(res) - 1
        res = res.lower()
        while left < right:
            if res[right] != res[left]:
                return False
            right -= 1
            left += 1
        return True        