class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        nums = [0 for _ in range(len(s) + 1)]

        for l, r, d in shifts:
            if d == 0:
                nums[l] -= 1
                nums[r + 1] += 1
            else:
                nums[l] += 1
                nums[r + 1] -= 1

        for i in range(len(s)):
            nums[i + 1] += nums[i]
        print(nums)

        for i in range(len(s)):
            nums[i] += ord(s[i]) - ord("a")


        index_char = nums[:len(s)]
        result = ""

        for n in index_char:
            result += chr((26 + n)%26 + ord("a"))

        print(index_char)

        return result
