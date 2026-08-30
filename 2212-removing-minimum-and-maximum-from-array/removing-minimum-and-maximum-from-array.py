class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        min_num = min(nums)
        max_num = max(nums)

        min_index = nums.index(min_num)
        max_index = nums.index(max_num)

        length = len(nums)

        first_turn_is_min_num = True if min(min_index + 1, length - min_index) < min(max_index + 1, length - max_index) else False

        result = 0

        if first_turn_is_min_num:

            from_start = True if min_index + 1 < length - min_index else False

            if from_start:
                result += min_index + 1 + min(max_index - min_index, length - max_index)
            else:
                result += length - min_index + min(max_index + 1, min_index - max_index)   
        else:
            from_start = True if max_index + 1 < length - max_index else False

            if from_start:
                result += max_index + 1 + min(min_index - max_index, length - min_index)
            else:
                result += length - max_index + min(min_index + 1, max_index - min_index)   
                
        return result