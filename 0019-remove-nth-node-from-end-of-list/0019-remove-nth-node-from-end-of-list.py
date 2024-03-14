# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        print(length)
        if length < n:
            return None
        else:
            ele = length - n + 1
            print(ele)
            prev = None
            count = 1
            temp = head
            if ele == 1:
                return head.next 
            else:
                while temp:
                    prev = temp
                    temp = temp.next
                    count += 1
                    if count == ele:
                        prev.next = temp.next
                        return head
                else:
                    return None

        


