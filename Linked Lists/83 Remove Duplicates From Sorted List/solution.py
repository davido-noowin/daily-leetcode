class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    current = head

    while current:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next

    return head