from operations import *

option = int(input('''
Given below are the various categories and their respective costs for the filling of the light bill

1. RGP : Residential General Purpose
2. GLP : General Lighting Purpose
3. Non-RGP : Low Tension Service for Commercial and Industrial Purpose
4. LTP (AG) : Agriculture Service
5. LTMD-1 : Low Tension Maximum Demand for Residential Purpose
6. LTMD-2 : Low Tension Maximum Demand for other than residential purpose
7. SL : Low Tension Tension Street Light Service
8. LEV : LT- Electric Vehicle Charging Stations
9. TMP : Low Tension Temporary Supply
10. HTMD-1 : High Tension Maximum Demand
11. HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC
12. HTMD-3 : High Tension Maximum Demand Temporary Supply
13. EV: HT- Electric Vehicle Charging Stations
14. HMTD - Metro Traction


Enter the code for selecting the category
'''))


if option == 1:
  from operations import case1
  
elif option == 2:
  from operations import case2

elif option == 3:
  from operations import case3

elif option == 4:
  from operations import case4

elif option == 5:
  from operations import case5

elif option == 6:
  from operations import case6

elif option == 7:
  from operations import case7

elif option == 8:
  from operations import case8

elif option == 9:
  from operations import case9

elif option == 10:
  from operations import case10

elif option == 11:
  from operations import case11
  
elif option == 12:
  from operations import case12

elif option == 13:
  from operations import case13
  
elif option == 14:
  from operations import case14
