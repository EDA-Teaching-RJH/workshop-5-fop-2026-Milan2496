

coinremain = 75
coincount = 0

while coincount < 75:

    coin = (input("A coffe costs 75p. Accepted coins = 50p, 20p, 10p, 5p. Please insert coin "))
    if coin == 50 or coin == 20 or coin == 10 or coin == 5:
        coin = int(coin)
        coincount = coincount + coin
        coinremain = coinremain - coin
        print(f"Balance inserted: {coincount}p")

        if coincount < 75:
            print(f"Balance left to pay: {coinremain}p")
        else:
            owe = coincount - 75
            print(f"Balance owed: {owe}p")
    else:
        print("Invalid input. This coin is not accepted")

fifty = 0
twenty = 0
ten = 0
five = 0

while owe > 50:
    owe = owe - 50
    fifty = fifty + 1

while owe > 20:
    owe = owe - 20
    twenty = twenty + 1

while owe > 10:
    owe = owe - 10
    ten = ten + 1

while owe > 5:
    owe = owe - 5
    five = five + 1

print(f"owed :")



