# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #use fast and slow pointers to find mid
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        #cut l1 
        slow.next = None

        #reverse from mid to tail
        prev = None
        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp

        #prev is now head of L2

        first = head
        second = prev
        #merge l1 and l2 
        #since l2 is shorter or equal
        while second:
            #save the next varaibles
            tmp1 = first.next 
            tmp2 = second.next
            #link
            first.next =  second
            second.next = tmp1
            #move forward
            first = tmp1
            second =tmp2


    



   



    