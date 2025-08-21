class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        stored = []

        def generate(temp):
            if len(temp) == n:
                stored.append(temp)
                return
            for char in ["a", "b", "c"]:
                if not temp or temp[-1] != char:
                    temp += char
                    generate(temp)
                    temp = temp[:len(temp) - 1]

        generate("")
        stored.sort()
    

        return stored[k-1] if len(stored) >= k else ""
