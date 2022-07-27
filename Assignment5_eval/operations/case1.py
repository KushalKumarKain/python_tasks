class One:
    def run():
        print(
            """
      You have chosen 1. RGP : Residential General Purpose
      """
        )
        InternalChoice = int(
            input(
                """
                           Choose from 
                           1:RGP(Residential General Purpose) 
                           OR 
                           2:BPL(Below Poverty Line)
                           """
            )
        )

        overallUnits = int(input("Enter the amount of units used : "))
        toc = int(
            input(
                """
                  Choose from 
                  1 = Energy Charges
                  OR
                  2 = Fixed Charges
                  """
            )
        )

        if InternalChoice == 1 and toc == 1 and overallUnits <= 50:
            result = (overallUnits * 320) / 100
            print(
                "Rate till first 50 units is 320 Paisa/unit. So, Your overall bill comes to be :  Rs ",
                result,
            )

        elif (
            InternalChoice == 1
            and toc == 1
            and (overallUnits > 50 and overallUnits <= 200)
        ):
            ind_units = overallUnits - 50
            result = ((ind_units * 395) + 16000) / 100
            print(
                "Rates after first 50 units and next 150 units is 395 Paisa/unit. So, Your overall bill comes to be :  Rs",
                result,
            )

        elif InternalChoice == 1 and toc == 1 and overallUnits > 200:
            ind_units = overallUnits - 200
            result = ((ind_units * 500) + 75250) / 100
            print(
                "Rates after first 200 units is 500 Paisa/unit. So, Your overall bill comes to be :  Rs",
                result,
            )

        elif InternalChoice == 1 and toc == 2:
            top = int(
                input(
                    """
                  Type of phase? 
                  1 = Single Phase , 
                  2 = Three Phase
                  """
                )
            )
            if top == 1:
                result = overallUnits * 25
                print(
                    "Rates for Single Phase is 25Rs/month/installation, hence your bill comes out to be Rs",
                    result,
                )

            elif top == 2:
                result = overallUnits * 65
                print(
                    "Rates for Single Phase is 65Rs/month/installation, hence your bill comes out to be Rs",
                    result,
                )

        elif InternalChoice == 2 and toc == 1 and overallUnits <= 50:
            result = (overallUnits * 150) / 100
            print(
                "Rate till first 50 units is 150 Paisa/unit. So, Your overall bill comes to be :  Rs",
                result,
            )

        elif (
            InternalChoice == 2
            and toc == 1
            and (overallUnits >= 51 and overallUnits < 200)
        ):
            ind_units = overallUnits - 50
            result = ((ind_units * 395) + 7500) / 100
            print(
                "Rates after first 50 units and next 150 units is 395 Paisa/unit. So, Your overall bill comes to be :  Rs",
                result,
            )

        elif InternalChoice == 2 and toc == 1 and overallUnits > 200:
            ind_units = overallUnits - 200
            result = ((ind_units * 500) + 66750) / 100
            print(
                "Rates after first 200 units is 500 Paisa/unit. So, Your overall bill comes to be :  Rs",
                result,
            )

        elif InternalChoice == 2 and toc == 2:
            result = overallUnits * 5
            print(
                "There is only Flat Phase available in this case so your bill comes out to be  Rs",
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
                if (toc or InternalChoice) != 1 | 2:
                    raise NumberError
                elif type(toc or InternalChoice) != int:
                    raise NumberError

            except NumberError:
                print("Invalid input")
