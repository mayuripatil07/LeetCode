class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if not version1 and not version2:
            return 0
        if not version1:
            return -1
        if not version2:
            return 1
        if len(version1) > 1:
            ver1 = version1.split('.')
        else:
            ver1 = [version1]
        if len(version2) > 1:
            ver2 = version2.split('.')
        else:
            ver2 = [version2]
        i = 0

        while(i < len(ver1) and i < len(ver2)):
            if int(ver1[i]) < int(ver2[i]):
                return -1
            if int(ver1[i]) > int(ver2[i]):
                return 1
            i += 1

        if i == len(ver1) and  i == len(ver2):
            return 0
        if i < len(ver1):
            while(i < len(ver1)):
                if int(ver1[i]) > 0:
                    return 1
                i += 1
            return 0
        if i < len(ver2):
            while(i < len(ver2)):
                if int(ver2[i]) > 0:
                    return -1
                i += 1
            return 0



                
