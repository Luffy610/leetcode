# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        nodes = []
        while temp:
            nodes.append(temp)
            temp = temp.next
        if len(nodes) == 1:
            return head
        nodes[k-1].val,nodes[-k].val = nodes[-k].val,nodes[k-1].val
        return head


        