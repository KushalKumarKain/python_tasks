class Two:
    def run():
        print("You have chosen 2. GLP : General Lighting Purpose")

        toc = int(
            input("Choose from 1 = Energy Charges | 2 = Fixed Charges"))

        overall_units = int(
            input("Enter the amount of units used : "))

        if toc == 1:
            if overall_units <= 200:
                result1 = (overall_units * 410) / 100
                print("Rate till first 200 units is 410 Paisa/unit."
                      "So, Your overall bill comes to be Rs ", result1)

            else:
                ind_units = overall_units - 200
                result = ((ind_units * 480) + 82000) / 100
                print("Rates after first 200 units is 500 Paisa/unit."
                      "So, Your overall bill comes to be :  Rs", result)

        elif toc == 2:
            top = int(
                input("Type of phase? 1 = Single Phase | 2 = Three Phase"))

            if top == 1:

                result = overall_units * 30
                print("Rates for Single Phase is 25Rs/month/installation."
                      "Hence your bill comes out to be  Rs", result)

            if top == 2:
                result = overall_units * 70
                print("Rates for Single Phase is 25Rs/month/installation."
                      "Hence your bill comes out to be  Rs", result)

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
