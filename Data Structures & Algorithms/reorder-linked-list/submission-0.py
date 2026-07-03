# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

  

        pre = None
        curr = slow
        while curr:
            curr_next = curr.next
            curr.next = pre
            pre = curr
            curr = curr_next
        
        h1 = head
        h2 = pre
        while  h2.next:
           h1_next = h1.next
           h2_next = h2.next

           h1.next = h2
           h2.next = h1_next

           h1 = h1_next
           h2 = h2_next
        
            


