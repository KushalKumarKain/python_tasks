print("You have chosen 6. LTMD-2 : Low Tension Maximum Demand for other than residential purpose")
                # int max_demand;
                # int c_demand;
                # int p_factor;
                
max_demand = int(input("Enter your maximum demand record during the month:  "))
                
                
if max_demand>0:
    c_demand = int(input("Enter the maximum KW for the supply of which TPL has provided facility to the consumer: ")*0.85)

  arr[3] = {max_demand, c_demand, 6}
  bill_demand = arr[0]

    for (i = 1; i < 3; i++)
      if (bill_demand < arr[i]):
        bill_demand = arr[i]
        print("Maximum Billng demand: ", bill_demand)

    print("Your Energy Charge Rs ", ((amt1*0.2) / 100))
    if (bill_demand <= 50):
      amt2 = bill_demand * 175;

    elif (bill_demand > 50 & bill_demand <= 80):
      amt2 = 7500+((bill_demand-50) * 230)

    elif (bill_demand > 80 & bill_demand <= c_demand):    
      amt2 = 14800 +((bill_demand-80) * 300)
            

    if(bill_demand>c_demand):        
      amt2 = (bill_demand-c_demand) * 425;

      print("Your Fixed Charge Rs ", amt2*0.2);
    
    p_factor = int(input("Enter your power factor(in percentage) "))
    
    if (p_factor > 90 & p_factor <= 95):
      amt3 = (p_factor-90) * 0.15;

    elif (p_factor > 95):
      amt3 = (100-p_factor) * 0.27;

    elif (p_factor < 90):
      amt3 = (90-p_factor) * 3;
            
        
    print("Your power factor Rs ", (amt3*0.2) / 100);
    amt = amt1 + amt2 + amt3;
    print("Electricity Bill Rs ", amt*0.2)
