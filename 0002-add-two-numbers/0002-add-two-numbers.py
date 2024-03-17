# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ""
        number2 = ""
        while l1:
            number1 += str(l1.val)
            l1 = l1.next
        while l2:
            number2 += str(l2.val)
            l2 = l2.next 
        number1 = number1[::-1]
        number2 = number2[::-1]
        res = int(number1) + int(number2)
        head = None
        prev = None
        if res == 0:
            head = ListNode(res)
            return head
        while res:
            val = res % 10
            node = ListNode(val)
            if head is None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node
            res = res // 10
        return head

        