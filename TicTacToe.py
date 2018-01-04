print('Good luck playing Tic Tac Toe !')

grid = [ [" "] * 3 for item in range(3)]

def pri():
    for item in range(3):
        print(grid[item])

def check_win():
    if (grid[0][0]== 'T' and grid[0][1]== 'T' and grid[0][2]== 'T') or (grid[1][0]== 'T' and grid[1][1]== 'T' and grid[1][2]== 'T') or (grid[2][0] == 'T' and grid[2][1] == 'T' and grid[2][2] == 'T') or  (grid[0][0] == 'T' and grid[1][0] == 'T' and grid[2][0] == 'T') or    (grid[0][1] == 'T' and grid[1][1] == 'T' and grid[2][1] == 'T') or    (grid[0][2] == 'T' and grid[1][2] == 'T' and grid[2][2] == 'T') or     (grid[0][0] == 'T' and grid[1][1] == 'T' and grid[2][2] == 'T') or      (grid[0][2] == 'T' and grid[1][1] == 'T' and grid[2][0] == 'T'):
        print("Player 2 won!")
        return True
    elif (grid[0][0]== 'O' and grid[0][1]== 'O' and grid[0][2]== 'O') or (grid[1][0]== 'O' and grid[1][1]== 'O' and grid[1][2]== 'O') or (grid[2][0] == 'O' and grid[2][1] == 'O' and grid[2][2] == 'O') or  (grid[0][0] == 'O' and grid[1][0] == 'O' and grid[2][0] == 'O') or    (grid[0][1] == 'O' and grid[1][1] == 'O' and grid[2][1] == 'O') or    (grid[0][2] == 'O' and grid[1][2] == 'O' and grid[2][2] == 'O') or     (grid[0][0] == 'O' and grid[1][1] == 'O' and grid[2][2] == 'O') or      (grid[0][2] == 'O' and grid[1][1] == 'O' and grid[2][0] == 'O'):
        print("Player 1 won!")
        return True
    else:
        return False

l=[]
f=list(range(1, 10))
while len(l) != 9 and check_win() != True:
    if len(l) % 2 == 0:
        p = int(input('Player1, Enter the number of block you want to play:'))
    else :
        p = int(input('Player 2, Enter the number of block you want to play:'))

    if p in l:
        print('That is not allowed, enter another block')
    elif p not in f:
        print('Enter a number from',[x for x in f if x not in l])
    else:
        l = l + [p]
        if len(l)%2 == 0:
            grid[(p-1)//3][(p-1)%3]='T'
        else:
            grid[(p-1)//3][(p-1)%3]='O'
        pri()


