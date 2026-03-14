
# Question 1
# Detect if a linked list has a cycle.
















def has_cycle(ll):
    # traverse at 1x and 2x speed, check for both nodes being the same
    slow = fast = ll

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False




# Question 2
# Find the middle node of a linked list.



















def find_mid(ll):
    slow = fast = ll

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
