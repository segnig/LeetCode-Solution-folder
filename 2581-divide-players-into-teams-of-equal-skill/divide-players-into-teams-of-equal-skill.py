class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sum_skill = skill[0] + skill[-1]

        right = len(skill) - 1

        result = 0
        for i in range(len(skill) // 2):
            if sum_skill != skill[i] + skill[right]:
                return -1
            result += skill[i] * skill[right]
            right -= 1
        return result