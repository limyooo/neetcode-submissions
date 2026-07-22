class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = False
        b = False
        c = False
        for i in triplets:
            if  i[0] > target[0] or i[1] > target[1] or i[2] > target[2]: 
                continue
            if i[0] == target[0]:
                a = True
            if i[1] == target[1]:
                b = True
            if i[2] == target[2]:
                c = True
        return a and b and c