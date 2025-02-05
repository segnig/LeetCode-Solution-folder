class Solution(object):
    def findRestaurant(self, list1, list2):
        index_list1 = defaultdict(lambda: 10000)
        index_list2 = defaultdict(lambda: 10000)

        for i, val in enumerate(list1):
            index_list1[val] = i

        for i, val in enumerate(list2):
            index_list2[val] = i


        index_sums = {}

        min_index = 2002


        for val in index_list1:
            index_sums[val] = index_list2[val] + index_list1[val]
            min_index = min(min_index, index_sums[val])

        result = [val for val in index_sums if index_sums[val] == min_index]

        return result
