import time
from abc import ABC, abstractmethod

class main_abstract(ABC):
    @abstractmethod
    def run(self):
        pass

number = int(input("Enter number of choice : "))

#####################################################
# defining a decorator function
def cal_time(func):    
    def inner1(*args):
 
        begin = time.time()
         
        func(*args)
 
        end = time.time()
        print("Total time taken for execution : /", end - begin, "/ seconds")
 
    return inner1
#####################################################

class fibo(main_abstract):
  @cal_time #placing the decorator.
  def run(self, number):
            
         n1, n2 = 0, 1
         count = 0

         if number <= 0:
            print("Please enter a positive integer")
         
         elif number == 1:
            print("Fibonacci sequence upto",number,":")
            print(n1)
         # generate fibonacci sequence
         else:
            time.sleep(2)
            print("Fibonacci sequence:")
            while count < number:
               print(n1)
               nth = n1 + n2
               # update values
               n1 = n2
               n2 = nth
               count += 1

F = fibo()
F.run(number)