"""
Problem Set 2.1
"""


# Problem 1: Swap Nodes in Pairs
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_nodes(head: ListNode) -> ListNode:
    """
    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
    
    Parameters:
        head (ListNode): head of linked list

    Returns:
        ListNode: new linked list after all adjacent nodes have been swapped
    """

    if head and head.next:
        temp = ListNode(next=head)
        previous_node, current_node = temp, head

        current_node = head
        while current_node and current_node.next:
            temp_next1 = current_node.next.next
            temp_next2 = current_node.next

            temp_next2.next = current_node
            current_node.next = temp_next1
            previous_node.next = temp_next2

            previous_node = current_node
            current_node = temp_next1
        
        return temp.next
    else:
        return head
