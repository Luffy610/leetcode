# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        sum = 0
        nodes = []
        new = None
        main = head
        while temp.next:
            if temp.val == 0:
                main.val = sum
                main = main.next 
                sum = 0
            else:
                sum += temp.val
            temp = temp.next 
        main.val = sum
        main.next = None
        return head