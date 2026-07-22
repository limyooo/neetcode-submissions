class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr = 0
        start = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0
        return start if total_gas >= 0 else -1