# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
            last = temp
        if length < k:
            index = length - k % length 
        else:
            index = length - k
        temp_index = 0
        if index == 0:
            return head
        temp = head
        prev = None
        while temp:
            if temp_index == index:
                prev.next = None
                temp_head = head
                head = temp
                last.next = temp_head
                break
            prev = temp
            temp_index += 1
            temp = temp.next
        return head
