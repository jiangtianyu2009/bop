# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counter = 1
        curnode = head
        while curnode.next is not None:
            counter = counter + 1
            curnode = curnode.next
        counter = counter // 2
        retnode = head
        while counter > 0:
            counter = counter - 1
            retnode = retnode.next
        return retnode
