print("You have chosen 5. LTMD-1 : Low Tension Maximum Demand for Residential Purpose \n");
                # int max_demand;
                # int c_demand;
                # int p_factor;

maxDemand = int(input("Enter your maximum demand record during the month:"))

if maxDemand>0:
	conDemand = int(input("Enter the maximum KW for the supply of which TPL has provided facility to the consumer:")*0.85)
  list[3] = {maxDemand, conDemand, 6}
    bill_demand = list
      for i = 1; i < 3; i+
			
        if bill_demand < [i] :
	        bill_demand = [i]

          print("maximum Billng demand: ", bill_demand);

                        int unit;
                        float amt1, amt2, amt3, amt;
    
                        printf("\n Your Energy Charge Rs:%0.2f", (amt1 / 100));
    
                            if (bill_demand <= 50)
                                {
                                    amt2 = bill_demand * 150;
                                }
                            
                            else if (bill_demand > 50 && bill_demand <= 80)
                                {
                                    amt2 = 7500+((bill_demand-50) * 185);
                                }

                            else if (bill_demand > 80 && bill_demand <= c_demand)
                                {
                                    amt2 = 14800 +((bill_demand-80) * 245);
                                }

                            if(bill_demand>c_demand)
                                {
                                    amt2 = (bill_demand-c_demand) * 350;
                                }
                
                                printf("\n Your Fixed Charge Rs:%0.2f", amt2);
                                printf("\nEnter your power factor(in percentage):");
                                scanf("%d", &p_factor);
                                

                            if (p_factor > 90 && p_factor <= 95)
                                {
                                    amt3 = (p_factor-90) * 0.15;
                                }
                            
                            else if (p_factor > 95)
                                {
                                    amt3 = (100-p_factor) * 0.27;
                                }

                                else if (p_factor < 90)
                                {
                                    amt3 = (90-p_factor) * 3;
                                }
                            
                            printf("\n Your power factor Rs:%0.2f", amt3 / 100);
                            amt = amt1 + amt2 + amt3;
                            printf("\n Electricity Bill RS :%0.2f", amt);