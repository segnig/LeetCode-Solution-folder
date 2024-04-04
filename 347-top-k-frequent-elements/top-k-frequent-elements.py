class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def_dict = defaultdict(int)
        for num in nums:
            def_dict[num] += 1
        def_dict = sorted(def_dict.items(), reverse=True, key=lambda x: x[1])
        print(def_dict)
        result = [k[0] for k in def_dict[:k]]
        return result
        