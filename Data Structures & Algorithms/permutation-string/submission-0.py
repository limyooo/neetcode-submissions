class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 > len(s1):
                char_left = s2[left]
                window[char_left] -= 1
                if window[char_left] == 0:
                    del window[char_left]
                left += 1
            if right - left + 1 == len(s1) and s1_count == window:
                return True
        return False

