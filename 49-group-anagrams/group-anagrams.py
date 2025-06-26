class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            word_list = (list(word))
            anagram_groups[tuple(sorted(word_list))].append(word)

        return [anagram_groups[word] for word in anagram_groups]   