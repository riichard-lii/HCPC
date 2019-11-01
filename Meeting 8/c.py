testcases = int(input())

for i in range(testcases):
    x = []
    lines = int(input())
    for j in range(lines):
        x.append(input())
    print(len(set(x)))