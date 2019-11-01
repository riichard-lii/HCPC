board = []
for i in range(5):
    board.append(list(input()))

def hi():
    a = 0
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'k':
                a += 1
                try:
                    if i-2 >= 0 and j-1 >= 0 and board[i-2][j-1] == 'k':
                        return False
                except IndexError:
                    pass
                try:
                    if i-1 >= 0 and j - 2 >= 0 and board[i-1][j-2] == 'k':
                        return False
                except IndexError:
                    pass
                try:
                    if i - 2 >= 0 and board[i-2][j+1] == 'k':
                        return False
                except IndexError:
                    pass
                try:
                    if i - 1 >= 0 and board[i-1][j+2] == 'k':
                        return False
                except IndexError:
                    pass
                try:
                    if j - 2 >= 0 and board[i+1][j-2] == 'k':
                        return False
                except IndexError:
                    pass
                try:
                    if board[i+1][j+2] == 'k':
                        return False
                except IndexError:
                    pass
                try:
                    if board[i+2][j+1] == 'k':
                        return False
                except IndexError:
                    pass
                try:
                    if j - 1 >= 0 and board[i+2][j-1] == 'k':
                        return False
                except IndexError:
                    pass
    return a == 9


thing = hi()
if thing:
    print("valid")
else:
    print("invalid")