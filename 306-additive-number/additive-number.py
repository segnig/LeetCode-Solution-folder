class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # if len(num) < 3: we cannot get the additive number
        if len(num) < 3:
            return False

        # generating every possible first number abd second number
        for index1 in range(1, len(num)):
            for index2 in range(index1+1, len(num)):
                first_num = num[: index1]
                second_num = num[index1 : index2]
                remain_num = num[index2 :]
                print(first_num, second_num, remain_num)
                if self.is_possible(first_num, second_num, remain_num):
                    return True

        return False

    def is_possible(self, first_num, second_num, remain_num):
        if len(remain_num) < max(len(first_num), len(second_num)):
            return False

        if (first_num[0] == "0" and len(first_num) != 1) or (second_num[0] == "0" and len(second_num) != 1):
            return False
        
        result = str(int(first_num) + int(second_num))

        if len(result) > len(remain_num):
            return False
        
        if result == remain_num[:len(result)]:
            if len(result) == len(remain_num):
                return True
            return self.is_possible(second_num, remain_num[:len(result)], remain_num[len(result):])

