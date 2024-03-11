# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        else:
            slow, fast, prev  = head, head, None
            while fast.next and fast.next.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if fast.next is None:
                mid = slow
            else:
                prev = slow
                mid = slow.next
            if mid.next is not None:
                prev.next = mid.next
            else:
                prev.next = None
            return head
