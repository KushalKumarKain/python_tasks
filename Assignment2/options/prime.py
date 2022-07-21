# from . import base
from base import main_abstract

number = int(input("Enter number of choice : "))
class prime(main_abstract):
   def run(self, number):

# Number is prime or not

    flag = False

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break

    if flag:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")
        
P = prime()
P.run(number)