class Solution(object):
    def groupAnagrams(self, strs):

        pair_anagrams = defaultdict(list)

        for word in strs:
            chars = list(word)
            chars.sort()
            chars = tuple(chars)

            pair_anagrams[chars].append(word) 

        result = [pair_anagrams[words] for words in pair_anagrams]

        return result
        
        