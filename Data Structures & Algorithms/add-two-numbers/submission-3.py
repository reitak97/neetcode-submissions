# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        dummy = ListNode()
        res = dummy
        while l1 or l2:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val

            if l2:
                val2 = l2.val


            total = val1+val2 + carry 
            digit = total % 10
            carry = total // 10 
            node = ListNode(digit)
            res.next = node
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            res.next = ListNode(carry)
        




        return dummy.next