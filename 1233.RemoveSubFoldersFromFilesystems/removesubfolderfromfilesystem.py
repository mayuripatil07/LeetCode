class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        result.append(folder[0])
        for i in range(1, len(folder)):
            if folder[i].startswith(result[-1] + '/'):
                continue
            else:
                result.append(folder[i])

        return result

                
