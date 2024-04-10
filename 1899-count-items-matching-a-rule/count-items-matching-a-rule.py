class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            i = 0
        elif ruleKey == "color":
            i = 1
        else:
            i = 2
        items = [k for k in items if ruleValue == k[i]]
        return len(items)