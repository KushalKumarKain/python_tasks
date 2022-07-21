# from . import base
from base import main_abstract

number = int(input("Enter number of choice : "))

class arm(main_abstract):
   def run(self, number):
     
    sum = 0

    temp = number
    while temp > 0:
      digit = temp % 10
      sum += digit ** len(str(number))
      temp //= 10

    # display the result
    if number == sum:
      print(number,"is an Armstrong number")
    else:
      print(number,"is not an Armstrong number")
      
A = arm()
A.run(number)
