class Twelve:
    def run():
        print("You chose 12. HTMD-3: HT Maximum Demand Temporary Supply")

        toc = int(
            input("Choose from 1 = Energy |2 = Fixed Charges|"
                  "3 = Power Factor | 4 = TOU Charge"))

        if toc == 1:
            overall_units = int(
                input("Enter the amount of kWs used upto 300 KW: "))
            result = (overall_units * 705) / 100
            print(
                "There is only Flat Phase available at 705 Paisa/unit."
                "So your bill comes out to be Rs", result)

        elif toc == 2:
            overall_units = int(input("Enter the amount of kWs used: "))
            a = int(
                input(
                    "Is it 1. Billing Demand up to contract demand|"
                    "2. Billing Demand in excess of contract demand"))

            if a == 1:
                result = overall_units * 25
                print("For this option, the rate is set to be 25 Rs/KW."
                      "So your bill comes to be Rs", result)
            elif a == 2:
                result = overall_units * 30
                print("For this option, the rate is set to be 30 Rs/KW."
                      "So your bill comes to be Rs", result)

        elif toc == 4:
            overall_units = int(input("Enter the amount of kWs used: "))
            result = (overall_units * 60) / 100
            print("There is only Flat Phase available at 60 Paisa/unit."
                  "So your bill comes out to be Rs", result)

        elif toc == 3:
            p_factor = int(input("Enter your power factor(in percentage): "))
            if p_factor > 90 & p_factor <= 95:
                amt1 = (p_factor - 90) * 0.15
            elif p_factor > 95:
                amt2 = (100 - p_factor) * 0.27
            elif p_factor < 90:
                amt3 = (90 - p_factor) * 3
            print("Your power factor Rs ", (amt3 * 0.2) / 100)
            amt = amt1 + amt2 + amt3
            print("Electricity Bill Rs ", amt * 0.2)

        else:

            class ErrorClass(Exception):
                """For all exceptions"""
            class NumberError(ErrorClass):
                """Raised when toc input is invalid"""

            try:
                if toc != 1 | 2:
                    raise NumberError
                elif not isinstance(toc, int):
                    raise NumberError

            except NumberError:
                print("Invalid input")
