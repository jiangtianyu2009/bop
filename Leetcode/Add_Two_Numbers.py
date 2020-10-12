# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def buildList(self, nums=[]):
        head = None
        for num in nums:
            if head is None:
                head = ListNode(num, None)
            else:
                node = ListNode(num, head)
                head = node
        return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    head = LinkedList().buildList([2, 4, 3])
    while head is not None:
        print(head.val)
        head = head.next
    assert Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert Solution().addTwoNumbers([0], [0]) == [0]
    assert Solution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [
        9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]
