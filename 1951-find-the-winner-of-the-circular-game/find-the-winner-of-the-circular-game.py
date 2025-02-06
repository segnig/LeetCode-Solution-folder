class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i + 1 for i in range(n)]
        index = 0

        while len(arr) > 1:
            removed_index = (index + k - 1) % len(arr)
            index = (index + k - 1) % len(arr)

            removed_element = arr[removed_index]
            arr.remove(removed_element)

        return arr[0]
        