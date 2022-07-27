class Nine:
    def run():
        print("You have chosen 9. TMP : Low Tension Temporary Supply")

        toc = int(
            input("Choose from1 = Fixed Charges |2 = Energy Charges"))

        if toc == 1:
            overall_units = int(input("Enter the amount of kWs used : "))
            result = overall_units * 25
            print("The rare here is FIXED and it is 25 kw/day"
                  "So your bill comes out to be Rs", result)

        elif toc == 2:
            overall_units = int(input("Enter the amount of kWs used : "))
            result = (overall_units * 510) / 100
            print("There is only Flat Phase at 510 Paisa/unit"
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
