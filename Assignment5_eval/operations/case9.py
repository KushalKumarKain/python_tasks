print('''
      You have chosen 9. TMP : Low Tension Temporary Supply
      ''')
toc = int(input('''
                Choose from
                1 = Fixed Charges
                OR
                2 = Energy Charges
                '''))

class Nine():
  def run(overallUnits):
    if toc==1:
      overallUnits = int(input("Enter the amount of kWs used : "))
      result=(overallUnits*25)
      print("The rare here is FIXED and it is 25 kw/day, so your bill comes out to be Rs", result)

    elif toc==2:
      overallUnits = int(input("Enter the amount of kWs used : "))
      result=(overallUnits*510)/100
      print("There is only Flat Phase, and the rate of it is 510 Paisa/unit, so your bill comes out to be Rs", result)
    
    else:
      class ErrorClass(Exception):
        """For all exceptions"""
        pass
      class NumberError(ErrorClass):
        """Raised when toc input is invalid"""
        pass
      try:
        if toc != 1 | 2 :
          raise NumberError 
        elif type(toc) != int:
          raise NumberError
        
      except NumberError:
        print("Invalid input")
          
        

Nine.run(toc)