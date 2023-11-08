import random

N = int(input("Enter number of coins: "))

coins = []

def coins_on_table(N):
    for i in range(N):
        coins.append(random.randint(0, 1))

def how_many_0(coins):
    count_0 = 0
    for coin in coins:
        if coin == 0:
            count_0 += 1
    return count_0
            
def how_many_1(coins):
    count_1 = 0
    for coin in coins:
        if coin == 1:
            count_1 += 1
    return count_1


coins_on_table(N)
print(coins)
zero = how_many_0(coins)
one = how_many_1(coins)

if zero < one:
    print(f"Flip over {zero} coins")
else:
    print(f"Flip over {one} coins")