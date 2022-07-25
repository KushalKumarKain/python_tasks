print("You have chosen 13. EV: HT- Electric Vehicle Charging Stations")
overallUnits = int(input("Enter the amount of units used : "))
toc = int(input("Choose from 1 = Energy Charges OR 2 = Demand Charges"))

if toc==1:
	result=(overallUnits*410)/100
	print("There is only Flat Phase available whose rate is 410 Paisa/unit, in this case so your bill comes out to be Rs", result)

if toc==2:
	top = int(input("What is your slab? 5 for Billing Demand up to contract demand , 6 for Billing Demand in excess of contract demand"))

	if top==5:
		result=overallUnits*25
		print("Rates for Billing Demand up to contract demand is 25Rs/month/KW, hence your bill comes out to be Rs",result)

	if top==6:			
		result=overallUnits*50
		print("Rates for Billing Demand in excess of contract demand is 50Rs/month/KW, hence your bill comes out to be Rs",result)
        