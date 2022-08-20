#didn't understand how we're supposed to do this problem
from math import floor

def middleNode(head):
    x = floor(len(head)/2)
    newhead = head[x:]
    return newhead


head = [1, 2, 3, 4, 5, 6]
print(middleNode(head))