from operations.case1 import One
from operations.case2 import Two
from operations.case3 import Three
from operations.case4 import Four
from operations.case5 import Five
from operations.case6 import Six
from operations.case7 import Seven
from operations.case8 import Eight
from operations.case9 import Nine
from operations.case10 import Ten
from operations.case11 import Eleven
from operations.case12 import Twelve
from operations.case13 import Thirteen
from operations.case14 import Fourteen

option = int(
    input(
        "Given below are the various categories and their respective costs for the filling of the light bill"
        "1. RGP : Residential General Purpose"
        "2. GLP : General Lighting Purpose"
        "3. Non-RGP : Low Tension Service for Commercial & Industrial Purpose"
        "4. LTP (AG) : Agriculture Service"
        "5. LTMD-1 : Low Tension Maximum Demand for Residential Purpose"
        "6. LTMD-2 : Low Tension Maximum Demand for other than residential purpose"
        "7. SL : Low Tension Tension Street Light Service"
        "8. LEV : LT- Electric Vehicle Charging Stations"
        "9. TMP : Low Tension Temporary Supply"
        "10. HTMD-1 : High Tension Maximum Demand"
        "11. HTMD-2 : High Tension Water and Sewage Pumping Stations run by AMC"
        "12. HTMD-3 : High Tension Maximum Demand Temporary Supply"
        "13. EV: HT- Electric Vehicle Charging Stations"
        "14. HMTD - Metro Traction"
        "Enter the code for selecting the category"))

dict = {
    1: One.run,
    2: Two.run,
    3: Three.run,
    4: Four.run,
    5: Five.run,
    6: Six.run,
    7: Seven.run,
    8: Eight.run,
    9: Nine.run,
    10: Ten.run,
    11: Eleven.run,
    12: Twelve.run,
    13: Thirteen.run,
    14: Fourteen.run,
}


def last():
    try:
        if option in dict.keys():
            dict[option]()
        else:
            raise ValueError
    except ValueError:
        print("Invalid Input")


last()
