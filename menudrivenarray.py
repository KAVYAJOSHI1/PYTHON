import numpy as np

def insert_element(arr, element, position):
    arr = np.insert(arr, position, element)
    return arr

def delete_element(arr, position):
    arr = np.delete(arr, position)
    return arr

def search_element_with_position(arr, x):
    indices = np.where(arr == x)[0]  # Get indices where x is found
    if indices.size > 0:
        position = indices[0] + 1  # Get the position (index + 1)
        print(f"ELEMENT FOUND AT POS {position}")
    else:
        print("ELEMENT NOT FOUND")

def print_array(arr):
    print("Current Array:", arr)

# Example usage and menu
array = np.array([10, 20, 30, 40, 50])

while True:
    print("\nMENU:")
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Search for an element and print its position")
    print("4. Print current array")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        element = int(input("Enter element to insert: "))
        position = int(input("Enter position to insert (0-based index): "))
        array = insert_element(array, element, position)
        print_array(array)
    elif choice == '2':
        position = int(input("Enter position to delete (0-based index): "))
        array = delete_element(array, position)
        print_array(array)
    elif choice == '3':
        x = int(input("Enter element to search: "))
        search_element_with_position(array, x)
    elif choice == '4':
        print_array(array)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
