class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        result = []
        for path in paths:
            i = path.split()
            root = i[0]
            for file in i[1:]:
                name, bracket, content = file.partition("(")
                hmap[content[:-1]].append(root + '/' + name)

        for key,values in hmap.items():
            if len(values) > 1:
                result.append(values)
        return result
