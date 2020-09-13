# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next==None or head.next.next == None:
            return head

        scndhead = temp = ListNode(head.next.val, head.next.next)
        frstHead = ListNode(head.val,head.next.next)
        while temp and temp.next:
          
            head.next = temp.next
            head = head.next
            
            
            temp.next = head.next
            temp = temp.next
        head.next = scndhead
        return frstHead