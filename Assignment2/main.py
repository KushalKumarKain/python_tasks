import options

print("This loop runs once only.")

while True:
    option = int(input('''
  1. Fibonacci Sequence 
  2. Armstrong Number 
  3. Prime Number
  Choose any one function : '''))

    if option == 1:
        print("You selected Fibonacci number")
        from options import fibonacci

    elif option == 2:
        print("You selected Armstrong number")
        from options import armstrong

    elif option == 3:
        print("You selected Prime number check")
        from options import prime

    else:
        print("Enter valid input and try again.")
