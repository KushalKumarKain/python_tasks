class Thirteen:
    def run():
        print("You chose 13. EV: HT- Electric Vehicle Charging Stations")

        toc = int(
            input("Choose from 1 = Energy Charges"
                  "2 = Demand Charges"))

        if toc == 1:
            overall_units = int(input("Enter the amount of units used : "))
            result = (overall_units * 410) / 100
            print("There is only Flat Phase available at 410 Paisa/unit."
                  "So your bill comes out to be Rs", result)

        elif toc == 2:
            overall_units = int(input("Enter the amount of units used : "))
            top = int(
                input(
                    "What is your slab?"
                    "1 for Billing Demand up to contract demand |"
                    "2 for Billing Demand in excess of contract demand"))

            if top == 1:
                result = overall_units * 25
                print(
                    "Rates for Billing Demand up to contract demand is 25Rs/month/KW."
                    "Hence your bill comes out to be Rs", result)

            elif top == 2:
                result = overall_units * 50
                print(
                    "Rates for Billing Demand in excess of contract demand is 50Rs/month/KW."
                    "Hence your bill comes out to be Rs", result)

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
