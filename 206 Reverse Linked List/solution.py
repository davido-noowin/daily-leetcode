# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: list[ListNode]) -> list[ListNode]:
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev