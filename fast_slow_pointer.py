
# Question 1
# Detect if a linked list has a cycle.







































def has_cycle(ll):
    # scan at 2x and 1x speed, check if they're ever the same
    fast = slow = ll

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False

def has_cycle(ll):
    # scan thru at 2x speed and 1x, check if they're the same

    fast = slow = ll

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            return True
    return False

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







































def find_mid_ll(ll):
    # scan at 2x speed and 1x, return 1x node when 2x reaches the end
    slow = fast = ll

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return None
    
    return slow

def find_mid(ll):
    # scan thru at 2x and 1x speed, return 1x when 2x reaches the end
    fast = slow = ll

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return None

    return slow

def find_mid(ll):
    slow = fast = ll

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return None
        
    return slow
