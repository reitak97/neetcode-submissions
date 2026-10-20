# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        carry = 0
       
        

        while l1 or l2:
            if l1:
                l1Val = l1.val
            else:
                l1Val = 0

            if l2:
                l2Val = l2.val
            else:
                l2Val = 0

            total = l1Val + l2Val + carry
            digit =  total % 10
            carry = total // 10

            cur.next = ListNode(digit) 
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        #leftover carry
        if carry:
            cur.next = ListNode(carry)

        return dummy.next
        

            