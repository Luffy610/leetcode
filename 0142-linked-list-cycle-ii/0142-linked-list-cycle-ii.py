# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []
        if head is None or head.next is None:
            return None
        else:
            temp = head
            while temp:
                if temp in visited:
                    return temp
                else:
                    visited.append(temp)
                    temp = temp.next
            return None
        