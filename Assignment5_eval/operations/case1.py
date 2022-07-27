class One:
    def run():
        print("You have chosen 1. RGP : Residential General Purpose")
        internal_choice = int(
            input("Choose 1:RGP(Residential General Purpose)|"
                  "2:BPL(Below Poverty Line)"))

        overall_units = int(input("Enter the amount of units used : "))
        toc = int(
            input("Choose from 1 = Energy Charges| 2 = Fixed Charges"))

        if internal_choice == 1 and toc == 1 and overall_units <= 50:
            result = (overall_units * 320) / 100
            print("Rate till first 50 units is 320 Paisa/unit."
                  "So, Your overall bill comes to be :  Rs ",result,)

        elif (
            internal_choice == 1
            and toc == 1
            and (overall_units > 50 and overall_units <= 200)
        ):
            ind_units = overall_units - 50
            result = ((ind_units * 395) + 16000) / 100
            print("Rates after first 50 units till 150 units = 395 Paisa/unit."
                  "So, Your overall bill comes to be :  Rs", result)

        elif internal_choice == 1 and toc == 1 and overall_units > 200:
            ind_units = overall_units - 200
            result = ((ind_units * 500) + 75250) / 100
            print("Rates after first 200 units is 500 Paisa/unit."
                  "So, Your overall bill comes to be :  Rs", result)

        elif internal_choice == 1 and toc == 2:
            top = int(
                input("Type of phase? 1 = Single Phase ,2 = Three Phase"))

            if top == 1:
                result = overall_units * 25
                print("Rates for Single Phase is 25Rs/month/installation."
                      "Hence your bill comes out to be Rs", result)

            elif top == 2:
                result = overall_units * 65
                print("Rates for Single Phase is 65Rs/month/installation."
                      "Hence your bill comes out to be Rs", result)

        elif internal_choice == 2 and toc == 1 and overall_units <= 50:
            result = (overall_units * 150) / 100
            print("Rate till first 50 units is 150 Paisa/unit."
                  "So, Your overall bill comes to be :  Rs", result)

        elif (
            internal_choice == 2
            and toc == 1
            and (overall_units >= 51 and overall_units < 200)
        ):
            ind_units = overall_units - 50
            result = ((ind_units * 395) + 7500) / 100
            print("Rates after first 50 units till 150 units = 395 Paisa/unit."
                  "So, Your overall bill comes to be :  Rs", result)

        elif internal_choice == 2 and toc == 1 and overall_units > 200:
            ind_units = overall_units - 200
            result = ((ind_units * 500) + 66750) / 100
            print(
                "Rates after first 200 units is 500 Paisa/unit."
                "So, Your overall bill comes to be :  Rs", result)

        elif internal_choice == 2 and toc == 2:
            result = overall_units * 5
            print("There is only Flat Phase available."
                  "So your bill comes out to be  Rs", result)

        else:

            class ErrorClass(Exception):
                """For all exceptions"""

            class NumberError(ErrorClass):
                """Raised when toc input is invalid"""

            try:
                if (toc or internal_choice) != 1 | 2:
                    raise NumberError
                elif type(toc or internal_choice) != int:
                    raise NumberError

            except NumberError:
                print("Invalid input")
