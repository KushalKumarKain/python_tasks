print('''
      You have chosen 2. GLP : General Lighting Purpose
      ''')
toc = int(input('''
                Choose from
                1 = Energy Charges
                OR
                2 = Fixed Charges
                '''))


class Two():
  def run(overallUnits):

    overallUnits = int(input("Enter the amount of units used : "))
                        
    if toc==1:
      if overallUnits <= 200:                                    
        result1 = (overallUnits*410)/100
        print("Rate till first 200 units is 410 Paisa/unit. So, Your overall bill comes to be Rs ", result1)
                                    
      else:
        ind_units=overallUnits-200
        result2=((ind_units*480)+82000)/100
        print("Rates after first 200 units is 500 Paisa/unit. So, Your overall bill comes to be :  Rs", result2)

    elif toc == 2:
      top = int(input('''Type of phase?
                      5 = Single Phase
                      6 = Three Phase
                      '''))
      if (top==5):
        result3=overallUnits*30
        print("Rates for Single Phase is 25Rs/month/installation, hence your bill comes out to be  Rs",result3)

      if (top==6):
        result4=overallUnits*70
        print("Rates for Single Phase is 25Rs/month/installation, hence your bill comes out to be  Rs",result4)
        
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
    
Two.run(toc)
