class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        left = 0
        for indx in spaces:
            result.append(s[left :indx])
            left = indx
        result.append(s[left:])
        
        return " ".join(result)

        