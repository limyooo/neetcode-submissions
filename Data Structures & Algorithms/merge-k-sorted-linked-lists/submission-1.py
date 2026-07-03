# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for head in lists:
            while head:
                heapq.heappush(min_heap,head.val)
                head = head.next
        
        dummy = ListNode(0)
        temp = dummy
        while min_heap:
            curr = ListNode(heapq.heappop(min_heap))
            temp.next = curr
            temp = curr
        return dummy.next
    #space ok , time o(n log k)
