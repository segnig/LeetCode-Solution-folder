class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        l = max(len(version1), len(version2))
        for i in range(l - len(version1)):
            version1.append("0")
        for i in range(l - len(version2)):
            version2.append("0")
        for i in range(l):
            if int(version1[i]) > int(version2[i]):
                return 1
            if int(version1[i]) < int(version2[i]):
                return -1 
        return 0  