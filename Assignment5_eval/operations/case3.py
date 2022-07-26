print('''
      You have chosen 3. Non-RGP : Low Tension Service for Commercial and Industrial Purpose
      ''')

toc = int(input('''
				Choose from
				1 = Energy Charges
				OR
				2 = Fixed Charges
				'''))

class Three():
  def run(overallUnits):

    if toc == 1:
      overallUnits = int(input("Enter the amount of units used : "))
      result = (overallUnits*460)/100
      print("There is only Flat Phase available in this case so your bill comes out to be  Rs", result)
  	
    elif toc == 2:
      top = int(input('''
                      What is your usage limit? 
                      3 for usage<=5 KW 
                      4 for usage>5KW & <= 15KW
                      '''))
      kwUsage = int(input("Enter the amount of KW power used (must be between 1 to 15): "))
      
      if top==3:
        result=kwUsage*70
        print("Rates for Single Phase is 70Rs/month/KW, hence your bill comes out to be  Rs",result)
      
      elif top==4:
        result=kwUsage*90
        print("Rates for Single Phase is 90Rs/month/KW, hence your bill comes out to be  Rs",result)

    else:
      class ErrorClass(Exception):
        """For all exceptions"""
        pass
      class NumberError(ErrorClass):
        """Raised when toc input is invalid"""
        pass
      
        if toc != 1 | 2 :
          print("Invalid input")
        elif type(toc) != int:
          print("Invalid type")
      raise NumberError
    
Three.run(toc)