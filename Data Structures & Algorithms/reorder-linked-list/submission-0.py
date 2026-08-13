# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse the 2nd half of the linked list
        #iterate over the lists and alternate adding a node to the new list

        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondHalf = slow.next
        slow.next = None #break apart from 1st half
        #now, slow points to the start of the 2nd half
        # reverse the list

        prev = None
        while secondHalf:
            tmp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = tmp
        second = prev

        first = head

        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        

        

