class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def_dict = defaultdict(list)
        for word in strs:
            w = word
            word = list(word)
            word.sort()
            word = str(word)
            def_dict[word].append(w)
        
        res = [def_dict[rs] for rs in def_dict]
        return res