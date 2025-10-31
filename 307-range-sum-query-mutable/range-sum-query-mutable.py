class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] + nums
        self.nums = nums

        for i in range(1, len(nums)):
            parent = i + (i & -i)
            if parent < len(self.tree):
                self.tree[parent] += self.tree[i]
        
        print(self.tree)
            

        

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val

        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index = index + (index & -index)

    def _calculate_sum(self, index):
        answer = 0

        while index > 0:
            answer += self.tree[index]
            index = index - (index & -index)
        return answer


    def sumRange(self, left: int, right: int) -> int:
        return self._calculate_sum(right + 1) - self._calculate_sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)