class Fourteen:
    def run():
        print(
            """
      You have chosen 14. HTMD - Metro Traction
      """
        )
        toc = int(
            input(
                """
                Choose from
                1 = Energy Charges
                OR
                2 = Fixed Charges
                OR
                3 = Power Factor
                OR
                4 = TOU Charge
                OR
                5 = Night Time (2200 Hrs To 0600 Hrs)
                """
            )
        )
        if toc == 1:
            overallUnits = int(input("Enter the amount of kWs used: "))
            result = (overallUnits * 355) / 100
            print(
                "There is only Flat Phase available in this case adn its rate is 355 Paisa/unit so your bill comes out to be Rs",
                result,
            )

        elif toc == 2:
            overallUnits = int(input("Enter the amount of kWs used: "))
            a = int(
                input(
                    "Is it 1. For Billing demand up to and including contract demand OR 2. For Billing demand in excess of contract demand"
                )
            )
            if a == 1:
                result = overallUnits * 335
                print(
                    "For this option, the rate is set to be 335/KW/month, so your bill comes to be Rs",
                    result,
                )
            elif a == 2:
                result = overallUnits * 385
                print(
                    "For this option, the rate is set to be 385/KW/month, so your bill comes to be Rs",
                    result,
                )

        elif toc == 4:
            overallUnits = int(input("Enter the amount of kWs used: "))
            result = (overallUnits * 60) / 100
            print(
                "There is only Flat Phase available in this case adn its rate is 60 Paisa/unit so your bill comes out to be Rs",
                result,
            )

        elif toc == 5:
            overallUnits = int(input("Enter the amount of kWs used: "))
            result = (overallUnits * 30) / 100
            print(
                "There is only Flat Phase available in this case adn its rate is 30 Paisa/unit so your bill comes out to be Rs",
                result,
            )

        elif Fourteen.toc == 3:
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
