print('''
      You have chosen 5. LTMD-2 : Low Tension Maximum Demand for other than residential purpose
      ''')

class Six:
    def run():
        try:
            kw_usage = float(input("enter number of units in KW for billing demand:"))
            j = int(input("enter contract demand in KW:"))
            k = float(input("enter power factor in percentage(%):"))

            if kw_usage < 0:
                raise ValueError
            elif (kw_usage > j):
                if kw_usage <= 50:
                    energy_charges = (kw_usage * 425) + (kw_usage * 4.80)
                else:
                    energy_charges = (kw_usage * 425) + (kw_usage * 5.00)
            elif kw_usage <= 50:
                energy_charges = (kw_usage * 175) + (kw_usage * 4.80)
            elif (kw_usage > 50 and kw_usage <= 80):
                energy_charges = ((50 * 175) + ((kw_usage - 50) * 230)) + (kw_usage * 5.00)
            elif (kw_usage > 80):
                energy_charges = ((50 * 175) + (30 * 230) + ((kw_usage - 80) * 300)) + (kw_usage * 5.00)

            if k < 0:
                raise ValueError
            elif (k > 100):
                raise ValueError
            elif k <= 90:
                total_amount = (kw_usage * 0.03) + energy_charges
                print(f'you have to pay {total_amount}Rs.')
            elif (k > 90 and k <= 95):
                total_amount = (kw_usage * 0.0015) + energy_charges
                print(f'you have to pay {total_amount}Rs.')
            elif (k > 95):
                total_amount = (kw_usage * 0.0027) + energy_charges
                print(f'you have to pay {total_amount}Rs.')
        except ValueError:
            print("invalid input!")

Six.run()
