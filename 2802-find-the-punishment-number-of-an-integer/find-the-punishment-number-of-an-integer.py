class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtrack(num, string, index, store):
            if index == len(string):
                total = sum([int(num) for num in store])
                stored = list()
                return total == num

            taked = backtrack(num, string, index + 1, store + [string[index]])
            not_taked = False

            if store:
                store[-1] += string[index]
                not_taked = backtrack(num, string, index + 1, store)
            return taked or not_taked

        result = 0

        for x in range(1, n +1):
            if backtrack(x, str(x*x), 0, []):
                result += x *x
        
        return result