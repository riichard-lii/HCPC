num = int(input())
for i in range(num):
    print(str(i+1), end='')
    students = input().split()[1::]
sum = 0
def check(kids):
    if len(kids) == 1: return []
    else:
        for i in check(kids[:-1]):
            if kids[0] < check
