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
            
            first_start = pre.next
            first_end = fast

            second_start = first_end.next
            #断开
            first_end.next = None
            #reverse firstgroup
            new_head = self.reverse(first_start)
            #pre跟新的头连接起来
            pre.next = new_head
            #让第一组的尾巴跟第二组的头连接起来
            first_start.next = second_start
            #开始反转第二组,pre 是开始前的一个点，所以是firsr——start，不能是second——start这样就跳过了
            pre = first_start
            

    def reverse(self,head):
        pre = None
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = pre
            pre = curr
            curr = curr_next
        return pre




