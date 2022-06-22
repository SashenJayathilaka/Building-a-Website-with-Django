price_of_house = 10000000
good_credit = True

if good_credit:
    down_payment = (price_of_house * 10) / 100
else:
    down_payment = (price_of_house * 20) / 100

print(f'Down Payment ${down_payment}')