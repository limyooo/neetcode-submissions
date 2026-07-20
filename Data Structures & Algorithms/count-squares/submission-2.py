class CountSquares:

    def __init__(self):
        self.square = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.square[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x,y = point
        ans = 0
        for (nx,ny),freq in self.square.items():
            if nx != x and ny != y and abs(x - nx) == abs(y - ny):
                ans += freq * self.square.get((x,ny),0) * self.square.get((nx,y),0)
        return ans
