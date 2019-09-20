record = input()
rank = 25
stars = 0
previous = False
streak = False

for i in record:
    if i == 'W':
        stars += 1
        if rank > 5 and previous:
            if streak:
                stars += 1
            else:
                streak = True
        else: previous = True

        if 21 <= rank <= 25:
            if stars > 2:
                stars -= 2
                rank -= 1
        elif 16 <= rank <= 20:
            if stars > 3:
                stars -= 3
                rank -= 1
        elif 11 <= rank <= 15:
            if stars > 4:
                stars -= 4
                rank -= 1
        elif 1 <= rank <= 10:
            if stars > 5:
                stars -= 5
                rank -= 1
        else:
            break
    else:
        previous = False
        streak = False
        if rank > 20:
            pass
        elif rank == 20:
            if stars != 0:
                stars -= 1
        elif 16 <= rank < 20:
                stars -= 1
                if stars == -1:
                    stars += 3
                    rank += 1
        elif 11 <= rank <= 15:
                if stars == -1:
                    stars += 4
                    rank += 1
        elif 1 <= rank <= 10:
                if stars == -1:
                    stars += 5
                    rank += 1
        else:
                break
if rank > 0:
    print(rank)
else: print("Legend")