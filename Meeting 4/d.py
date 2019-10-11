num = int(input())
l = input().split()
n = int(l[0])
my = [n]
for i in l:
    if int(i) > n:
        n = int(i)
        my.append(n)
print(len(my))
a = ''
for i in my:
    a += str(i) + ' '
print(a[:-1])