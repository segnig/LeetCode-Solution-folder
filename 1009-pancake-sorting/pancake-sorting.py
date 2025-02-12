class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        right = len(arr) - 1
        nums = arr.copy()
        nums.sort()

        while right >= 0:
            if nums[right] == arr[right]:
                right -= 1

            else:
                left = right
                while left >= 0:
                    if nums[right] == arr[left]:
                        result.append(left+1) 
                        arr = arr[:left + 1][::-1] + arr[left+1:]
                        result.append(right + 1)
                        arr = arr[:right + 1][::-1] + arr[right+1:]
                        break
                    left -= 1

        return result 