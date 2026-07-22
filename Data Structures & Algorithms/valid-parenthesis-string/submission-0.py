class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left = 0
        max_left = 0
        for ch in s:
            if ch =='(':
                min_left += 1
                max_left += 1
            elif ch == '*':
                min_left -= 1
                max_left += 1
            else:
                min_left -= 1
                max_left -= 1
            if max_left < 0:
                return False
            min_left = max(min_left,0)
        return min_left == 0

