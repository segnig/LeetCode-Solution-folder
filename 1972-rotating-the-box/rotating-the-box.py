class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row, col = len(boxGrid), len(boxGrid[0])
        result = [["."] * row for _ in range(col)]

        for r in range(row):
            place = col - 1
            for c in reversed(range(col)):
                if boxGrid[r][c] == "*":
                    result[c][row - r - 1] = "*"
                    place = c - 1
                elif boxGrid[r][c] == "#":
                    result[place][row - r - 1] = "#"
                    place -= 1
                
        return result
        