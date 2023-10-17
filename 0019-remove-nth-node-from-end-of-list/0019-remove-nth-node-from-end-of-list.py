# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        init = head
        count = 1
        while init.next:
            count+=1
            init = init.next
        
        index_to_remove = count - n - 1
        if index_to_remove < 0:
            return head.next
        dummy = ListNode(0, head)
        init = dummy
        index = 0
        while init:
            if index == index_to_remove:
                head.next = head.next.next
            init = init.next
            if head.next:
                head = head.next
            else:
                break
            index+=1

        return dummy.next