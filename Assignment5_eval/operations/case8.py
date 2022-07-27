class Eight:
    def run():
        print("You have chosen 8.LEV : LT- Electric Vehicle Charging Stations")

        toc = int(
            input("Choose from 1 = Fixed Charges| 2 = Energy Charges"))

        if toc == 1:
            overall_units = int(input("Enter the amount of units used : "))
            result = overall_units * 25
            print("The rare here is FIXED and it is 340 Paisa/unit."
                  "So your bill comes out to be Rs", result)

        elif toc == 2:
            overall_units = int(input("Enter the amount of units used : "))
            result = (overall_units * 420) / 100
            print("There is only Flat Phase at 340 Paisa/unit"
                  "So your bill comes out to be Rs", result)

        else:

            class ErrorClass(Exception):
                """For all exceptions"""

            class NumberError(ErrorClass):
                """Raised when toc input is invalid"""

            try:
                if toc != 1 | 2:
                    raise NumberError
                elif type(toc) != int:
                    raise NumberError

            except NumberError:
                print("Invalid input")
