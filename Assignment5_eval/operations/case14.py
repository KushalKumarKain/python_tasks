class Fourteen:
    def run():
        print(
            """
      You have chosen 14. HTMD - Metro Traction
      """
        )
        toc = int(
            input("Choose"
                  "1 = Energy Charges | 2 = Fixed Charges | 3 = Power Factor"
                  "4 = TOU Charge | 5 = Night Time (2200 Hrs To 0600 Hrs)"))

        if toc == 1:
            overall_units = int(input("Enter the amount of kWs used: "))
            result = (overall_units * 355) / 100
            print("There is only Flat Phase available at 355 Paisa/unit."
                  "So your bill comes out to be Rs", result)

        elif toc == 2:
            overall_units = int(input("Enter the amount of kWs used: "))
            a = int(
                input("1. For Billing demand up to including contract demand |"
                      "2. For Billing demand in excess of contract demand"))
            if a == 1:
                result = overall_units * 335
                print("For this option, the rate is set to be 335/KW/month."
                      "So your bill comes to be Rs", result)
            elif a == 2:
                result = overall_units * 385
                print("For this option, the rate is set to be 385/KW/month."
                      "So your bill comes to be Rs", result)

        elif toc == 4:
            overall_units = int(input("Enter the amount of kWs used: "))
            result = (overall_units * 60) / 100
            print("There is only Flat Phase available at 60 Paisa/unit."
                  "So your bill comes out to be Rs", result)

        elif toc == 5:
            overall_units = int(input("Enter the amount of kWs used: "))
            result = (overall_units * 30) / 100
            print("There is only Flat Phase available at 30 Paisa/unit."
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
            print("Electricity Bill RS ", amt * 0.2)
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
