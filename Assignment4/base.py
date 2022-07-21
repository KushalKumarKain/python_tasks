from abc import ABC, abstractmethod
import time

class main_abstract(ABC):
    @abstractmethod
    def run(self):
        pass
    
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
