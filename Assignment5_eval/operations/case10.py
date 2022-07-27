# pylint: disable=no-else-raise
class Ten:
    def run():
        print("You have chosen 10. HTMD-1 : High Tension Maximum Demand")

        toc = int(
            input(
                "1 = Energy| 2 = Fixed Charges| 3 = Power"
                "Factor| 4 = TOU Charge| 5 = Night Time"
            )
        )

        if toc == 1:
            overall_units = int(input("Enter the amount of kWs used : "))

        elif overall_units <= 400:
            result = (overall_units * 455) / 100
            print(
                "Rate till first 400 units is 455 Paisa/unit."
                "So, Your overall bill comes to be Rs ",
                result,
            )

        elif overall_units >= 401:
            ind_units = overall_units - 400
            result = ((ind_units * 445) + 182000) / 100
            print(
                "Rates after first 400 units and above is 445 Paisa/unit."
                "So, Your overall bill comes to be Rs",
                result,
            )

        elif toc == 2:
            overall_units = int(
                input("Enter the amount of kWs used upto 1000 KW: "))
            if overall_units <= 1000:
                result = overall_units * 260
                print(
                    "Rate till first 50 units is 260 Rs/KW."
                    "So, Your overall bill comes to be Rs ",
                    result,
                )
            elif overall_units >= 1001 & overall_units <= 2000:
                ind_units = overall_units - 1000
                result = (ind_units * 335) + 260000
                print(
                    "Rates after first 1000 KW and till 2000 KW is 335 Rs/KW."
                    "So, Your overall bill comes to be Rs",
                    result,
                )
            elif overall_units > 2000:
                result = ind_units * 385
                print(
                    "Rates after 2000 KW is 385 Rs/KW."
                    "So, Your overall bill comes to be Rs",
                    result,
                )

        elif toc == 3:
            p_factor = int(
                input("Enter your power factor(in percentage): "))
            if p_factor > 90 & p_factor <= 95:
                amt1 = int((p_factor - 90) * 0.15)
            elif p_factor > 95:
                amt2 = int((100 - p_factor) * 0.27)
            elif p_factor < 90:
                amt3 = int((90 - p_factor) * 3)
            print("Your power factor Rs ", (amt3 * 0.2) / 100)
            amt = amt1 + amt2 + amt3
            print("Electricity Bill Rs ", amt * 0.2)

        elif toc == 4:
            overall_units = int(
                input("Enter the amount of kWs used upto 300 KW: "))
            if overall_units <= 300:
                result = (overall_units * 80) / 100
                print(
                    "Rate till first 50 units is 260 Paisa /unit."
                    "So, Your overall bill comes to be Rs ",
                    result,
                )
            elif overall_units >= 300:
                ind_units = overall_units - 300
                result = ((ind_units * 100) + 24000) / 100
                print(
                    "Rates after first 300 KW is 100 Paisa/unit."
                    "So, Your overall bill comes to be Rs",
                    result,
                )

        elif toc == 5:
            overall_units = int(
                input("Enter the amount of kWs used upto 300 KW: "))
            result = (overall_units * 30) / 100
            print(
                "There is only Flat Phase available."
                "In this case adn its rate is 30 Paisa/unit."
                "So your bill comes out to be Rs",
                result,
            )

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
