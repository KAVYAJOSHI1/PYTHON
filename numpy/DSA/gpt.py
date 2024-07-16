# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the node
        self.next = next  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    def insert_beg(self, value):
        """
        Insert a new element with value 'value' at the beginning of the linked list.
        """
        new_node = ListNode(value)  # Create a new node with the given value
        new_node.next = self.head   # Link the new node to the current head
        self.head = new_node        # Update the head to point to the new node

    def insert_end(self, value):
        """
        Insert a new element with value 'value' at the end of the linked list.
        """
        new_node = ListNode(value)  # Create a new node with the given value
        if not self.head:
            self.head = new_node    # If the list is empty, make the new node the head
            return

        current = self.head
        while current.next:
            current = current.next  # Traverse to the end of the linked list
        current.next = new_node    # Link the last node to the new node

    def insert_at_position(self, value, position):
        """
        Insert a new element with value 'value' at the specified position in the linked list.
        Position is 0-based, meaning position 0 is the head of the list.
        """
        if position < 0:
            raise ValueError("Position must be non-negative")

        new_node = ListNode(value)  # Create a new node with the given value

        if position == 0:
            new_node.next = self.head   # Link the new node to the current head
            self.head = new_node        # Update the head to point to the new node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next

        if current is None:
            raise IndexError("Position out of bounds")

        new_node.next = current.next   # Link the new node to the next node at position
        current.next = new_node        # Link the current node to the new node

    def print_list(self):
        """
        Print the linked list elements.
        """
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_beg(1)        # Insert 1 at the beginning
    ll.insert_end(3)        # Insert 3 at the end
    ll.insert_at_position(2, 1)  # Insert 2 at position 1 (after 1)
    ll.print_list()         # Expected output: 1 -> 2 -> 3 -> None
