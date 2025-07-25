def perform_operation(num1, num2, operation):
 if operation=="add":
    return num1 + num2

 elif operation=="subtract":
    return num1 - num2

 elif operation=="multiply":
    return num1 * num2

 elif operation=="divide":
    if b == 0:
        return "Cannot divide by zero"
    return num1 / num2
 else:
        return "Invalid operation"
