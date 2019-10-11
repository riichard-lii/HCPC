num = int(input())
for i in range(num):
    a = input()
    if a == "P=NP":
        print("skipped")
    else:
        b = a.split('+')
        print(int(b[0]) + int(b[1]))