print('''
      You have chosen 5. LTMD-1 : Low Tension Maximum Demand for Residential Purpose
      ''')

class Five:
    def run():
        try:
            kw_usage = float(input("Enter number of units in KW for billing demand: "))
            j = int(input("Enter contract demand in KW: "))
            k = float(input("Enter power factor in percentage(%): "))

            if kw_usage < 0:
                raise ValueError
            elif (kw_usage > j):
                if kw_usage <= 50:
                    energy_charges = (kw_usage * 425) + (kw_usage * 4.65)
                else:
                    energy_charges = (kw_usage * 425) + (kw_usage * 4.80)
            elif kw_usage <= 50:
                energy_charges = (kw_usage * 150) + (kw_usage * 4.65)
            elif (kw_usage > 50 and kw_usage <= 80):
                energy_charges = ((50 * 150) + ((kw_usage - 50) * 185)) + (kw_usage * 4.80)
            elif (kw_usage > 80):
                energy_charges = ((50 * 150) + (30 * 185) + ((kw_usage - 80) * 245)) + (kw_usage * 4.80)

            if k < 0:
                raise ValueError
            elif (k > 100):
                raise ValueError
            elif k <= 90:
                total_amount = (kw_usage * 0.03) + energy_charges
                print(f'The total bill comes out to be {total_amount}Rs.')
            elif (k > 90 and k <= 95):
                total_amount = (kw_usage * 0.0015) + energy_charges
                print(f'The total bill comes out to be {total_amount}Rs.')
            elif (k > 95):
                total_amount = (kw_usage * 0.0027) + energy_charges
                print(f'The total bill comes out to be {total_amount}Rs.')
        except ValueError:
            print("invalid input!")


Five.run()