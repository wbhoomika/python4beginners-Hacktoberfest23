# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    dummy = ListNode(-1)
    current = dummy

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    # If one of the lists is not empty, append it to the merged list
    if l1 is not None:
        current.next = l1
    elif l2 is not None:
        current.next = l2

    return dummy.next

# Helper function to print the merged linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
# Creating sorted linked lists: 1 -> 3 -> 5 and 2 -> 4 -> 6
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

print("First sorted list:")
print_list(list1)

print("Second sorted list:")
print_list(list2)

merged_list = merge_sorted_lists(list1, list2)
print("Merged sorted list:")
print_list(merged_list)
