# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        self.node=[]
        ptr = head2 = ListNode(0)
        if head:
            temp = ListNode(head.val, head.next)
        else:
            return head
        while temp:
            self.node.append(temp.val)
            temp = temp.next
        for x in sorted(self.node):
            ptr.next = ListNode(x)
            ptr = ptr.next
        return head2.next