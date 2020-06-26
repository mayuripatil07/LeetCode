class ProductOfNumbers:

    def __init__(self):
        self.data = []

    def add(self, num: int) -> None:
        if num != 1:
            for i in range(len(self.data)-1, -1, -1):
                if self.data[i] == 0:
                    break
                self.data[i] *= num
        self.data.append(num)

    def getProduct(self, k: int) -> int:
        return self.data[-k]




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
