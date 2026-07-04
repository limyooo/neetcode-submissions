# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while True:
            fast = pre
            for _ in range(k):
                fast = fast.next
                if not fast:
                    return dummy.next
            start = pre.next
            end = fast

            second_start = fast.next
            end.next = None

            new_head = self.reverse(start)

            pre.next = new_head

            start.next = second_start

            pre = start


    
    def reverse(self,head):
        pre = None
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = pre
            pre = curr
            curr = curr_next
        return pre
