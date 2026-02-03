# functional requirement
# code must acceot only 50 20 10 5 as inputs
# code must output the correct balance owed 

# non functional requirement
# if a string is inputted then it must ask the user to try again



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



