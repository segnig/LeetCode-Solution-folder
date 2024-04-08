class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        sol = []
        while i<n1 and j<n2:
            if nums1[i] < nums2[j]:
                sol.append(nums1[i])
                i += 1
            else:
                sol.append(nums2[j])
                j += 1
        sol.extend(nums1[i:])
        sol.extend(nums2[j:])

        if len(sol) % 2 == 0:
            return (sol[len(sol)//2-1] + sol[len(sol)//2]) / 2
        else:
            return float(sol[len(sol)//2])  