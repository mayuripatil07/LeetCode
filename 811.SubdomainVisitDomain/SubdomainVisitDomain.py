class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hmap = {}
        result = []
        for i in cpdomains:
            j = 1
            a = i.replace(" ",".").split(".")
            n = len(a)
            c = i.split(" ")
            if c[1] in hmap:
                hmap[c[1]] += int(a[0])
            else:
                hmap[c[1]] = int(a[0])
            while(j < n-1):
                a.pop(1)
                b = ".".join(a[1:])
                if b in hmap:
                    hmap[b] += int(a[0])
                else:
                    hmap[b] = int(a[0])
                j += 1

        for key, value in hmap.items():
            string = str(value) + " " + key
            result.append(string)
        return result
            
