class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        seq_num = "123456789"

        result = []

        for left in range(9):
            for right in range(left + 1, 10):
                num = int(seq_num[left:right])

                if low <= num <= high:
                    result.append(num)

        return sorted(result)