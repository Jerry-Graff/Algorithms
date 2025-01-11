"""
A 2D hash map can be used to represent grids, graphs or nested structures.
Usefull if you need to store mutiple strings of data without collision
e.g. phone book, grocery prices.
"""
graph = {
    "A": {"apple": 0.15, "avacado": 1.12},
    "B": {"bannana": 0.55, "beans": 1.75},
    "C": {"carrot": 0.19, "corn": 0.90},
    "D": {"dates": 3.95, "duck": 6.95},
    "E": {"eggs": 2.95, "edamame": 4.99},
    }

print(graph["E"]["eggs"])

"""
A hash map can also link to a more complex data structure like a linked list.
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


hash_to_list = {}

hash_to_list["group1"] = ListNode(1, ListNode(2, ListNode(3)))

# Traversing and printing the linked list at "group1"
node = hash_to_list["group1"]
while node:
    print(node.value, end=" -> ")
    node = node.next
# Output: 1 -> 2 -> 3 ->
