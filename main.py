from art import logo

print(logo)
#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1,n2):
  return n1/n2

math_ops = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# function = math_ops["+"]
# print(function(1,2))

def calculator():
  num1 = float(input("What's the first number?: "))
  
  for op in math_ops:
    print(op)
  
  should_continue = True
  while should_continue:
    
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calc_function = math_ops[operation_symbol]
    answer = calc_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
      
    user_continue = input(f"Type 'y' to keep calculating with {answer} or type 'n' to start a new calculation: ")
    if user_continue == "n":
      should_continue = False
      calculator()
    else:
      num1 = answer

calculator()

