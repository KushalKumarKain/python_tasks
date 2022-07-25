print("You have chosen 9. TMP : Low Tension Temporary Supply")
toc = int(input("Choose from 1 = Fixed Charges OR 2 = Energy Charges"))
overallUnits = int(input("Enter the amount of kWs used : "))

if toc==1:
  result=(overallUnits*25)
  print("The rare here is FIXED and it is 25 kw/day, so your bill comes out to be Rs", result)

if toc==2:
  result=(overallUnits*510)/100
  print("There is only Flat Phase, and the rate of it is 510 Paisa/unit, so your bill comes out to be Rs", result)
