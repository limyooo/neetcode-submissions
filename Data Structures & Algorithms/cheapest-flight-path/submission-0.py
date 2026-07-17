class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minprices = [float('inf')] * n
        minprices_copy = []
        minprices[src] = 0
        for _ in range(k+1):
            minprices_copy = minprices.copy()
            flag = False
            for curr,nxt,cost in flights:
                if minprices[nxt] > minprices_copy[curr] + cost:
                    minprices[nxt] = minprices_copy[curr] + cost
                    flag =True
            if flag == False:
                break
        
        return minprices[dst] if minprices[dst] != float('inf') else -1
