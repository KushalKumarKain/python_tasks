class Eight:
    def run(overallUnits):
        print(
            """
      You have chosen 8.LEV : LT- Electric Vehicle Charging Stations
      """
        )
        toc = int(
            input(
                """Choose from
                1 = Fixed Charges
                OR
                2 = Energy Charges
                """
            )
        )

        if toc == 1:
            overallUnits = int(input("Enter the amount of units used : "))
            result = overallUnits * 25
            print(
                "The rare here is FIXED and it is 340 Paisa/unit, so your bill comes out to be Rs",
                result,
            )

        elif toc == 2:
            overallUnits = int(input("Enter the amount of units used : "))
            result = (overallUnits * 420) / 100
            print(
                "There is only Flat Phase, and the rate of it is 340 Paisa/unit, so your bill comes out to be Rs",
                result,
            )

        else:

            class ErrorClass(Exception):
                """For all exceptions"""

                pass

            class NumberError(ErrorClass):
                """Raised when toc input is invalid"""

                pass

            try:
                if toc != 1 | 2:
                    raise NumberError
                elif type(toc) != int:
                    raise NumberError

            except NumberError:
                print("Invalid input")
