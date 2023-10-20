# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head) or head.next == None or head.next.next == None:
            return False
        pointer_1 = head.next
        pointer_2 = head.next.next
        while pointer_1 != pointer_2:
            if pointer_2 == None or pointer_2.next == None or pointer_2.next.next == None:
                return False
            
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
        
        return True

