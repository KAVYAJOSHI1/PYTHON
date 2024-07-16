# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the node
        self.next = next  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    def insert(self, val):
        """
        Insert a new element with value 'val' at the end of the linked list.
        """
        new_node = ListNode(val)  # Create a new node with the given value
        if not self.head:
            # If the linked list is empty, make the new node the head
            self.head = new_node
        else:
            # Otherwise, traverse to the end of the linked list and insert the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Link the last node to the new node

    def insert_at_position(self, val, position):
        """
        Insert a new element with value 'val' at the specified position in the linked list.
        Position is 0-based, meaning position 0 is the head of the list.
        """
        new_node = ListNode(val)  # Create a new node with the given value
        if position == 0:
            # If inserting at the head (position 0), link the new node to the current head and update head
            new_node.next = self.head
            self.head = new_node
        else:
            # Traverse the list to find the insertion point
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of bounds")
                current = current.next
            # Insert the new node by adjusting the pointers
            new_node.next = current.next
            current.next = new_node

    def print_list(self):
        """
        Print the linked list elements.
        """
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

def main():
    ll = LinkedList()
    
    while True:
        print("\nChoose an option:")
        print("1. Insert at end")
        print("2. Insert at specific position")
        print("3. Print list")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter the value to insert: "))
            ll.insert(val)
        elif choice == '2':
            val = int(input("Enter the value to insert: "))
            position = int(input("Enter the position to insert (0-based index): "))
            try:
                ll.insert_at_position(val, position)
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == '3':
            ll.print_list()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
