# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            
            val = v1 + v2 + carry
            carry = val //10
            val %= 10
            cur.next = ListNode(val)
            cur = cur.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        #consider if last carry such as 8 + 7
        if carry:
            cur.next = ListNode(carry)
        return dummy.next