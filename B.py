n = int(input())
boba = input().split(' ')
a = input()
types = input()
toppings = []
for i in range(n) :
    toppings.append(input().split()[1::])
money = int(input())

combination = []
for i, price in enumerate(boba):
    for j in toppings[i]:
        combination.append(int(price) + int(j))
per = min(combination)

print(max(int(money) // per - 1,0))