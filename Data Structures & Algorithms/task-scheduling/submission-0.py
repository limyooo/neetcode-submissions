class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
            count_task = max(count)
            max_task = count.count(count_task)
        return max(len(tasks),(count_task - 1) * (n+1) + max_task)