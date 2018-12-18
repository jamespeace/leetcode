# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        currentNode = head = ListNode(0)

        while node1 and node2:
            if node1.val > node2.val:
                currentNode.next = node2
                node2 = node2.next
            else:
                currentNode.next = node1
                node1 = node1.next
            currentNode = currentNode.next
        currentNode.next = node1 or node2
        return head.next

def printList(l):
    s = ''
    h = l.next
    s += str(l.val)
    while h is not None:
        s += '->' + str(h.val)
        h = h.next
    print(s)
# list 1->2->4
n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(4)
printList(n1)
# list 1->3->4
n2 = ListNode(1)
n2.next = ListNode(3)
n2.next.next = ListNode(4)
printList(n2)
# merge lists
s = Solution()
n3 = s.mergeTwoLists(n1, n2)
printList(n3)