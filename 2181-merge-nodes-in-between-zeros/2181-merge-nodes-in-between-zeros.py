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
        pprev = None
        while temp:
            if temp.val == 0:
                node = ListNode(sum)
                if new is None:
                    new = node
                    prev = node
                else:
                    prev.next = node
                    prev = node
                sum = 0
            else:
                sum += temp.val
            temp = temp.next 
        return new