width = int(input())
num = int(input())
sum = 0
for i in range(num):
    c = input().split()
    a = int(c[0])
    b = int(c[1])
    sum += a * b
print(int(sum / width))