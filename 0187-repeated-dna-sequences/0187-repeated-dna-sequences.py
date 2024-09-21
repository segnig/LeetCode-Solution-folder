class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()
        if len(s) < 10:
            return []
        left, right = 0, 10
        store = set()
        while right < len(s)+1:
            if s[left:right] in store:
                result.add(s[left:right])
            store.add(s[left:right])
            left, right = left + 1, right + 1
        
        return list(result)
