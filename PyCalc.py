import numpy as np

# Define a dictionary for operations
# sets and matches operators up with their numpy equation
operations = {
    '+': np.add,
    '-': np.subtract,
    '*': np.multiply,
    '/': np.divide,
    '**': np.power
}


def evaluate_expression(expression):
    # Remove spaces from the expression
    expression = expression.replace(' ', '')

    # iterates through the operations
    # if it exists split left and right side based on op
    # sets left and right values to float
    # returns operation calculation of left and right side
    for op in operations.keys():
        if op in expression:
            left, right = expression.split(op)
            left, right = float(left), float(right)
            return operations[op](left, right)
    return None

# enter input
# try to evaluate and print results
# if cant grab exception and print out exp
exp = input("Enter an expression ('x' to exit): ")
while exp != 'x':
    try:
        result = evaluate_expression(exp)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"Invalid expression: {e}")
    exp = input("Enter an expression ('x' to exit): ")