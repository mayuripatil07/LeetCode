class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.s = 0
        self.count = 0
        self.size = size

    def next(self, val: int) -> float:
        self.s += val
        self.count += 1
        self.q.append(val)
        if self.count > self.size:
            value = self.q.popleft()
            self.s -= value
            self.count -= 1
        return self.s/self.count
