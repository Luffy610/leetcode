#Optimal Approach T.C: O(N) S.C.: O(1)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        size = 1

        # calculating length and making a circular loop
        while curr.next is not None:
            curr = curr.next
            size += 1

        curr.next = head

        # cut from the rotating point
        i = size - (k % size)

        while i > 1:
            head = head.next
            i -= 1

        curr = head.next
        head.next = None
        return curr