width = int(input())
num = int(input())
sum = 0
x = []
for i in range(num):
    c = input().split()
    x.append((int(c[0]), int(c[1])))
for j in x:
    sum += j[0] * j[1]
print(int(sum / width))
