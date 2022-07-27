class Seven:
    def run():
        print(
            """
      You have chosen 7. SL : Low Tension Tension Street Light Service
      """
        )
        overallUnits = int(input("Enter the amount of units used : "))
        if overallUnits > 0:
            result = (overallUnits * 430) / 100
            print(
                """There is only Flat Phase, and the rate of it is 340 Paisa/unit, so your bill comes out to be Rs """,
                result,
            )
        else:
            if overallUnits < 0:

                class ErrorClass(Exception):
                    """For all exceptions"""

                    pass

                class NumberError(ErrorClass):
                    """Raised when toc input is invalid"""

                    pass

                print("Invalid input!!")
                raise NumberError
