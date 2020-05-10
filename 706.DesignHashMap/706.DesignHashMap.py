class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = []


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for i in self.hmap:
            if i[0] == key:
                i[1] = value
            else:
                continue
        self.hmap.append([key,value])



    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for i in self.hmap:
            if i[0] == key:
                return i[1]
            elif i[0] != key:
                continue
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i in self.hmap:
            if i[0] == key:
                i[1] = -1
