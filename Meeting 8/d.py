n = int(input())
peeps = []
for i in range(n):
    peeps.append(input().split())
print(peeps)
minn = 99999999999999
#sum1 = sum(map(lambda x: float(x[2]), peeps))
for i, peep in enumerate(peeps):
    minn = min(minn, float(peep[1]) + )
print(minn)