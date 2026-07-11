# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        #now slow points to mid
        slow.next = None


        #reverse second half
        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp

        #head of second is prev

        l2 = prev
        first =head
        #merge halfs
        while l2:
            #store next before breaking
            tmp1 = first.next
            tmp2 = l2.next

            first.next = l2 
            l2.next =  tmp1
            first = tmp1
            l2 = tmp2




        

        