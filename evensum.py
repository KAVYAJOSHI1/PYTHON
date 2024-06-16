for i in range(100, 200):
    
    num = i
    total_sum = 0  # Changed 'sum' variable name to 'total_sum' to avoid conflict with built-in function sum()
    while num > 0:
        digit = num % 10
        total_sum = total_sum + digit
        num = num // 10  # Used integer division to update 'num' correctly

    if total_sum % 2 != 0:
        print(i)
  