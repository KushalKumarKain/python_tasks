print("You have chosen 3. Non-RGP : Low Tension Service for Commercial and Industrial Purpose")

toc = int(input('''
				Choose from
				1 = Energy Charges
				OR
				2 = Fixed Charges
				'''))

overallUnits = int(input("Enter the amount of units used : "))
                        
if toc==1:
	result1=(overallUnits*460)/100
	print("There is only Flat Phase available in this case so your bill comes out to be  Rs", result1);

if toc==2:
	top = int(input('''What is your usage limit? 
									5 for usage<=5 KW 
									6 for usage>5KW & <= 15KW
									'''))
	if top==5:	
		result2=overallUnits*70
		print("Rates for Single Phase is 70Rs/month/KW, hence your bill comes out to be  Rs",result2)	
  
	if top==6:	
		result3=overallUnits*90
		print("Rates for Single Phase is 90Rs/month/KW, hence your bill comes out to be  Rs",result3)
