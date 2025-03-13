class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        first_player, second_player = self.helper(nums, turn = 0)

        return first_player >= second_player

    def helper(self, nums, turn):
        if len(nums) == 1:
            if turn % 2 == 0:
                return (nums[0], 0)
            else:
                return (0, nums[0])

        from_left = self.helper(nums[1:], turn + 1)
        from_right = self.helper(nums[:-1], turn + 1)

        if turn % 2 == 0:
            left = (from_left[0] + nums[0], from_left[1])
            right = (from_right[0] + nums[-1], from_right[1])

            return left if left[0] > right[0] else right

        left = (from_left[0], from_left[1] + nums[0])
        right = (from_right[0], from_right[1] + nums[-1])

        return left if left[1] > right[1] else right
        
