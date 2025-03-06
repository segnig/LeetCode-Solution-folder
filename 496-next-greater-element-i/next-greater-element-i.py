class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)

        val_to_index = {
            val: index for index, val in enumerate(nums1)
        }
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                num = stack.pop()
                if num in val_to_index:
                    result[val_to_index[num]] = nums2[i]
            stack.append(nums2[i])

        return result