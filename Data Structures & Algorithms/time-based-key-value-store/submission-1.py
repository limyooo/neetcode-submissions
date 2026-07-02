class TimeMap:

    def __init__(self):
        self.dict =defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
       self.dict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        res = ""
        arr = self.dict[key]
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                left += 1
            else:
                right -= 1
        return res

        
