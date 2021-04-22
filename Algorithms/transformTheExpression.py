'''
Transform the algebraic expression with brackets into RPN form
    (Reverse Polish Notation).
Two-argument operators: +, -, *, /, ^ (priority from the lowest to highest),
    brackets (). 
Operands: only letters: a,b,...,z. Assume that there is only one RPN form
    (no expressions like a*b*c)

Note: text grouped in [] does not appear in the input file
'''

# number of expressions:
T = int(input())
expressions = []
for i in range(T):
    expressions.append(input())

operators = '+-*/^'
brackets = '()[]'
# to contain operators
stack = []
output = ''
result = []

# if element is a letter, add right away to the output
# if element is an operator, add to the stack
# if element is an open bracket, add to the stack
# if element is a closed bracket, pop the stack to ouput until the open bracket
# do not add brackets to the output
# if there is nothing left in the expression, pop the rest of the stack to the output
# finally, add the output to result before setting it back to an empty string
    # to prepare for the next expression
for expression in expressions:
    for symbol in expression:
        if symbol.isalpha():
            output += symbol
        if symbol in operators:
            stack.append(symbol)
        if symbol == '(':
            stack.append(symbol)
        if symbol == ')':
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()
    result.append(output)
    output = ''

for thing in result:
    print(thing)