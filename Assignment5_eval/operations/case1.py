print("You have chosen 1. RGP : Residential General Purpose")

InternalChoice = int(input('''
                           Choose from 
                           1:RGP(Residential General Purpose) 
                           OR 
                           2:BPL(Below Poverty Line)
                           '''))

# if (InternalChoice==1):
#   toc = int(input('''
#                   Choose from 
#                   3 = Energy Charges
#                   OR
#                   4 = Fixed Charges
#                   '''))
#   overallUnits = int(input("Enter the amount of units used : "))

#   if(toc==3):        
#     if (overallUnits<=50):
#       result1 = (overallUnits*320)/100
#       print("Rate till first 50 units is 320 Paisa/unit. So, Your overall bill comes to be :  Rs ", result1)
#     elif overallUnits>50 and overallUnits<=200:
#       ind_units=overallUnits-50
#       result2 = ((ind_units*395)+16000)/100
#       print("Rates after first 50 units and next 150 units is 395 Paisa/unit. So, Your overall bill comes to be :  Rs", result2)
#     else:
#         ind_units=overallUnits-200
#         result3=((ind_units*500)+75250)/100
#         print("Rates after first 200 units is 500 Paisa/unit. So, Your overall bill comes to be :  Rs", result3)



#   if (toc==4):
#     top = int(input('''
#                     Type of phase? 
#                     5 = Single Phase , 
#                     6 = Three Phase
#                     '''))
#     if (top == 5):
#       result4 = overallUnits*25
#       print("Rates for Single Phase is 25Rs/month/installation, hence your bill comes out to be Rs",result4)
#     if (top==6):
#       result5=overallUnits*65
#       print("Rates for Single Phase is 65Rs/month/installation, hence your bill comes out to be Rs",result5)

# if (InternalChoice==2):
#   toc = int(input('''
#                   Choose from
#                   7 = Energy Charges
#                   OR
#                   8 = Fixed Charges
#                   '''))
  
#   if toc==7:
#     overallUnits = int(input("Enter the amount of units used : "))
#     if (overallUnits<=50):
#       result6 = (overallUnits*150)/100
#       print("Rate till first 50 units is 150 Paisa/unit. So, Your overall bill comes to be :  Rs", result6)
#     elif overallUnits>=51 and overallUnits<200:
#       ind_units=overallUnits-50
#       result7 = ((ind_units*395)+7500)/100
#       print("Rates after first 50 units and next 150 units is 395 Paisa/unit. So, Your overall bill comes to be :  Rs", result7)
#     elif overallUnits>=201: 
#       ind_units=overallUnits-200
#       result8 = ((ind_units*500)+66750)/100
#       print("Rates after first 200 units is 500 Paisa/unit. So, Your overall bill comes to be :  Rs", result8)
  
#   if toc==8:
#       overallUnits = int(input("Enter the amount of units used : "))
#       result9=(overallUnits*5)
#       print("There is only Flat Phase available in this case so your bill comes out to be  Rs", result9)





class One():
  # def run(self, InternalChoice, toc, overallUnits):
  #   pass
  
  def run(InternalChoice):
    overallUnits = int(input("Enter the amount of units used : "))
    toc = int(input('''
                  Choose from 
                  1 = Energy Charges
                  OR
                  2 = Fixed Charges
                  '''))
    
    if InternalChoice == 1 and toc == 1 and overallUnits<=50:
      result = (overallUnits*320)/100
      print("Rate till first 50 units is 320 Paisa/unit. So, Your overall bill comes to be :  Rs ", result)

    elif InternalChoice == 1 and toc == 1 and (overallUnits>50 and overallUnits<=200):
      ind_units=overallUnits-50
      result = ((ind_units*395)+16000)/100
      print("Rates after first 50 units and next 150 units is 395 Paisa/unit. So, Your overall bill comes to be :  Rs", result)
      
    elif InternalChoice == 1 and toc == 1 and overallUnits>200:
      ind_units = overallUnits-200
      result = ((ind_units*500)+75250)/100
      print("Rates after first 200 units is 500 Paisa/unit. So, Your overall bill comes to be :  Rs", result)


    elif InternalChoice == 1 and toc == 2:
      top = int(input('''
                  Type of phase? 
                  1 = Single Phase , 
                  2 = Three Phase
                  '''))
      if top == 1:
        result = overallUnits*25
        print("Rates for Single Phase is 25Rs/month/installation, hence your bill comes out to be Rs",result)
      
      elif top == 2:
        result = overallUnits*65
        print("Rates for Single Phase is 65Rs/month/installation, hence your bill comes out to be Rs",result)
    
    elif InternalChoice == 2 and toc == 1 and overallUnits<=50:
      result = (overallUnits*150)/100
      print("Rate till first 50 units is 150 Paisa/unit. So, Your overall bill comes to be :  Rs", result)
    
    elif InternalChoice == 2 and toc == 1 and (overallUnits>=51 and overallUnits<200):
      ind_units=overallUnits-50
      result = ((ind_units*395)+7500)/100
      print("Rates after first 50 units and next 150 units is 395 Paisa/unit. So, Your overall bill comes to be :  Rs", result)
      
    elif InternalChoice == 2 and toc == 1 and overallUnits>200:
      ind_units = overallUnits-200
      result = ((ind_units*500)+66750)/100
      print("Rates after first 200 units is 500 Paisa/unit. So, Your overall bill comes to be :  Rs", result)

    elif InternalChoice == 2 and toc == 2:
      result = (overallUnits*5)
      print("There is only Flat Phase available in this case so your bill comes out to be  Rs", result)

    else:
      class ErrorClass(Exception):
        """For all exceptions"""
        pass
      class NumberError(ErrorClass):
        """Raised when toc input is invalid"""
        pass
      try:
        if (toc or InternalChoice) != 1 | 2 :
          raise NumberError 
        elif type(toc or InternalChoice) != int:
          raise NumberError
        
      except NumberError:
        print("Invalid input")

# one = One()
# one.InternalChoice()
One.run(InternalChoice)



