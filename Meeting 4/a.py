a = input().split()
capacity = float(a[0])
rate = float(a[1])
distance = float(a[2])
speeds = []
yes = False
for i in range(6):
    b = input().split()
    speeds.append((float(b[0]), float(b[1])))
for i in speeds[::-1]:
    hours = distance / i[0]
    fuel = distance / i[1] + hours * rate
    if fuel * 2 <= capacity:
        print("YES", int(i[0]))
        yes = True
        break
if not yes: print("NO")