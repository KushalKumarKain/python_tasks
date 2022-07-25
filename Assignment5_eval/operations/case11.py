print("You have chosen 11. HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC \n")
toc = int(input("Choose from 1 = Energy OR 2 = Fixed Charges OR 3 = Power Factor OR 4 = TOU Charge 5 = Night Time \n"))

if toc==1:

	overallUnits = int(input("Enter the amount of kWs used upto 300 KW: "))
	result = (overallUnits*410)/100
	print("There is only Flat Phase available in this case adn its rate is 410 Paisa/unit so your bill comes out to be Rs", result)

if toc==2:
	overallUnits= int(input("Enter the amount of kWs used: "))
	a = int(input("Is it 1. Fix charge/KW of billing Demand / month OR 2. Excess Demand"))
	if a==1:
		result = (overallUnits*225)
		print("For this option, the rate is set to be 225/KW, so your bill comes to be money",result)
	elif a==2:
		result = (overallUnits*285)
		print("For this option, the rate is set to be 285/KW, so your bill comes to be money",result)

if toc==4:
	overallUnits= int(input("Enter the amount of kWs used: "))
	result=(overallUnits*60)/100
	print("There is only Flat Phase available in this case adn its rate is 60 Paisa/unit so your bill comes out to be Rs", result);  

if toc==5:
	
			overallUnits= int(input("Enter the amount of kWs used: "))
			result=(overallUnits*30)/100
			print("There is only Flat Phase available in this case adn its rate is 30 Paisa/unit so your bill comes out to be Rs", result)

if toc==3:

	p_factor = int(input("Enter your power factor(in percentage): "))
							
	if p_factor > 90 & p_factor <= 95:			
		amt1 = (p_factor-90) * 0.15
	
	elif p_factor > 95:
		amt2 = (100-p_factor) * 0.27
	
	elif p_factor < 90:
		amt3 = (90-p_factor) * 3

	print("Your power factor Rs ", (amt3*0.2) / 100)
	amt = amt1 + amt2 + amt3
	print("Electricity Bill Rs ", amt*0.2)
