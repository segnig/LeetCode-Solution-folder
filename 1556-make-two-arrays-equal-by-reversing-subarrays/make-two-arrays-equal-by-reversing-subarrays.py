from collections import Counter

class Solution:
    def canBeEqual(self, target, arr):
        counter_target, counter_arr = Counter(target), Counter(arr)
        for num in counter_arr:
            if num not in counter_target or counter_target[num] != counter_arr[num]:
                return False
        return True


