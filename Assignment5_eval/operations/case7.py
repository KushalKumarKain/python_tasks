class Seven:
    def run():
        print("You chose 7. SL : Low Tension Tension Street Light Service")

        overall_units = int(input("Enter the amount of units used : "))
        if overall_units > 0:
            result = (overall_units * 430) / 100
            print("There is only Flat Phase at 340 Paisa/unit."
                  "So your bill comes out to be Rs ", result)
        else:
            if overall_units < 0:

                class ErrorClass(Exception):
                    """For all exceptions"""

                class NumberError(ErrorClass):
                    """Raised when toc input is invalid"""

                print("Invalid input!!")
                raise NumberError
