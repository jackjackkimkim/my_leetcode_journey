from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):

        # defining a blank res variable
        res = ""

        # initializing ptr to head
        ptr = self.head

        # traversing and adding it to res
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next

        # removing trailing commas
        res = res.strip(", ")

        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


l1 = LinkedList()
l2 = LinkedList()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
l1.head = node1
node1.next = node2
node2.next = node3

print(l1)


node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
l2.head = node4
node4.next = node5
node5.next = node6

print(l2)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        current = dummy = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next


sol = Solution().mergeTwoLists(node1, node4)
print(l2)
