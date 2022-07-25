print("You have chosen 4. LTP (AG) : Agriculture Service")

toc = int(input('''Choose from
                1 = Energy Charges
                OR
                2 = Minimum Charges
                '''))
overallUnits = int(input("Enter the amount of units used : "))
if toc==1:
  result=(overallUnits*340)/100
  print("There is only Flat Phase, and the rate of it is 340 Paisa/unit, so your bill comes out to be Rs", result)

if toc==2:
	result=(overallUnits*10)
	print("There is only per bhp phase, and the rate of it is 10 Rs/unit, so your bill comes out to be Rs", result)
