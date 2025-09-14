class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        numscopy = nums1[:m:]

        idx1 = 0
        idx2 = 0


        for i in  range(m + n):
            if idx1 >= m:
                nums1[i] = nums2[idx2]
                idx2 += 1
            
            elif idx2 >= n:
                nums1[i] = numscopy[idx1]
                idx1 += 1
            elif numscopy[idx1] > nums2[idx2]:
                nums1[i] = nums2[idx2]
                idx2 += 1
            else:
                nums1[i] = numscopy[idx1]
                idx1 += 1