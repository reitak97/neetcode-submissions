class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head
        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow= slow.next

        slow.next = slow.next.next

        return dummy.next