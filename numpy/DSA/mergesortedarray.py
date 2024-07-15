def issorted(lst):
    """
    Check if a list is sorted in non-decreasing order.
    
    Parameters:
    lst (list): The input list to be checked.
    
    Returns:
    bool: True if the list is sorted, False otherwise.
    """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def merge(list1, n, list2, m):
    """
    Merge two sorted lists list1 and list2 into list1 in sorted order.
    
    Parameters:
    list1 (list): First sorted list with extra space to accommodate list2.
    n (int): Number of elements in list1.
    list2 (list): Second sorted list.
    m (int): Number of elements in list2.
    """
    i = n - 1  # Pointer for list1
    j = m - 1  # Pointer for list2
    k = n + m - 1  # Pointer for merged list (list1)

    # Merge list1 and list2 from the end
    while i >= 0 and j >= 0:
        if list1[i] > list2[j]:
            list1[k] = list1[i]
            i -= 1
        else:
            list1[k] = list2[j]
            j -= 1
        k -= 1
    
    # If there are remaining elements in list2, they need to be copied into list1
    while j >= 0:
        list1[k] = list2[j]
        j -= 1
        k -= 1

# Main program
list1 = []
list2 = []

print("ENTER THE SIZE FOR LIST 1:")
n = int(input())
print("ENTER THE SIZE FOR LIST 2:")
m = int(input())

if n > 0 and m > 0:
    print("ENTER THE ELEMENTS FOR LIST 1 (in sorted order):")
    for i in range(n):
        list1.append(int(input(f"Element {i + 1}: ")))
    print(list1)
    
    print("ENTER THE ELEMENTS FOR LIST 2 (in sorted order):")
    for i in range(m):
        list2.append(int(input(f"Element {i + 1}: ")))
    print(list2)
    
    if issorted(list1) and issorted(list2):
        list1.extend([0] * m)  # Extend list1 to accommodate list2
        merge(list1, n, list2, m)
        print("SORTED LIST AFTER MERGING IS:")
        print(list1)
    else:
        print("LISTS ARE NOT SORTED")
else:
    print("INVALID INPUT")
