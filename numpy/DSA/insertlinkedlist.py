class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList: 
    def __init__(self):
        self.head = None
     
    def insert_beg(self, value):  
        new_node = ListNode(value)
        new_node.next = self.head  
        self.head = new_node
        print("NODE INSERTED AT BEGINNING SUCCESSFULLY")
     
    def insert_end(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print("NODE INSERTED AT END SUCCESSFULLY")

    def insert_pos(self, value, pos):
        new_node = ListNode(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            print("NODE INSERTED AT POSITION", pos, "SUCCESSFULLY")
            return
        current = self.head
        for i in range(pos - 1):
            if current is None:
                print("INVALID POSITION")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node
        print("NODE INSERTED AT POSITION", pos, "SUCCESSFULLY")

    def display(self):
            if not self.head:
                print("LIST IS EMPTY")
                return
            current=self.head
            while current:
                print(current.value,end = " -> ")
                current = current.next
            print("None")

def main():
    obj = LinkedList()
    while True:
        print("1. INSERT AT BEGINNING")
        print("2. INSERT AT END")
        print("3. INSERT AT SPECIFIED POSITION")
        print("4. DISPLAY LIST")
        print("5. EXIT")
        ch = int(input("ENTER YOUR CHOICE: "))
        if ch == 1:
            val = int(input("ENTER THE VALUE: "))
            obj.insert_beg(val)
        elif ch == 2:
            val = int(input("ENTER THE VALUE: "))
            obj.insert_end(val)
        elif ch == 3:
            val = int(input("ENTER THE VALUE: "))
            pos = int(input("ENTER THE POSITION: "))
            obj.insert_pos(val, pos)
        elif ch==4:
            obj.display()
        elif ch == 5:
            break
        else:
            print("INVALID CHOICE")

if __name__ == "__main__":
    main()
