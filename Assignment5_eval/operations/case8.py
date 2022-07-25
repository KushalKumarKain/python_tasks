print("You have chosen 8.LEV : LT- Electric Vehicle Charging Stations")

toc = int(input('''Choose from
                1 = Fixed Charges
                OR
                2 = Energy Charges
                '''))

overallUnits = int(input("Enter the amount of units used : "))
if toc==1:
	
	result=(overallUnits*25)
	print("The rare here is FIXED and it is 340 Paisa/unit, so your bill comes out to be Rs", result)

if toc==2:

	result=(overallUnits*420)/100
	print("There is only Flat Phase, and the rate of it is 340 Paisa/unit, so your bill comes out to be Rs", result)
