class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()

        left, right = 0, len(skill) - 1
        result = 0
        test = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] == test:
                result += skill[left] * skill[right]
            else:
                return -1
            left, right = left + 1, right - 1

        return result    