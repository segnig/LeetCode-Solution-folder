class Solution(object):
    def printVertically(self, s):
        mx_len = max([len(word) for word in s.split()])
        result = [[] for _ in range(mx_len)]

        for word in s.split():
            for index in range(mx_len):
                if index < len(word):
                    result[index].append(word[index])
                else:
                    result[index].append(" ")

        res = ["".join(chars) for chars in result]
        result = []

        for word in res:
            lenght = len(word) - 1
            while lenght and word[lenght] == " ":
                lenght -= 1
            result.append(word[:lenght + 1])

        return result