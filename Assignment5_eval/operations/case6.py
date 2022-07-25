# case 6:
#             { printf("You have chosen 6. LTMD-2 : Low Tension Maximum Demand for other than residential purpose \n");
#                 int max_demand;
#                 int c_demand;
#                 int p_factor;
                
#                 printf("Enter your maximum demand record during the month:  \n");
#                 scanf("%d", &max_demand);
                
#                 if(max_demand>0)
#                     {
                    
#                     printf("Enter the maximum KW for the supply of which TPL has provided facility to the consumer:  \n");
#                     scanf("%d", &c_demand);
                    
#                     c_demand = c_demand * 0.85;
        
#                     int arr[3] = {max_demand, c_demand, 6};
#                     int bill_demand = arr[0];

#                         for (int i = 1; i < 3; i++)
#                             {
#                                 if (bill_demand < arr[i])
#                                 {
#                                 bill_demand = arr[i];
#                                 }
#                             }

#                         printf("Maximum Billng demand:%d \n", bill_demand);

#                         int unit;
#                         float amt1, amt2, amt3, amt;
    
#                         printf("\n Your Energy Charge Rs:%0.2f", (amt1 / 100));
    
#                             if (bill_demand <= 50)
#                                 {
#                                     amt2 = bill_demand * 175;
#                                 }
                            
#                             else if (bill_demand > 50 && bill_demand <= 80)
#                                 {
#                                     amt2 = 7500+((bill_demand-50) * 230);
#                                 }

#                             else if (bill_demand > 80 && bill_demand <= c_demand)
#                                 {
#                                     amt2 = 14800 +((bill_demand-80) * 300);
#                                 }

#                             if(bill_demand>c_demand)
#                                 {
#                                     amt2 = (bill_demand-c_demand) * 425;
#                                 }
                
#                                 printf("Your Fixed Charge Rs: %0.2f \n", amt2);
                                
#                             printf("Enter your power factor(in percentage):  \n");
#                             scanf("%d", &p_factor);
                                
#                             if (p_factor > 90 && p_factor <= 95)
#                                 {
#                                     amt3 = (p_factor-90) * 0.15;
#                                 }
                            
#                             else if (p_factor > 95)
#                                 {
#                                     amt3 = (100-p_factor) * 0.27;
#                                 }

#                                 else if (p_factor < 90)
#                                 {
#                                     amt3 = (90-p_factor) * 3;
#                                 }
                            
#                             printf("Your power factor Rs: %0.2f  \n", amt3 / 100);
#                             amt = amt1 + amt2 + amt3;
#                             printf("Electricity Bill RS :%0.2f  \n ", amt);
#                     }
#             }
