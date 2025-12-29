#Program to determine if, given two places on a chessboard, can a knight move from one place to another in 2 moves.
def GenMoves(x,y):
    L = [(x+2,y+1),(x+2,y-1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2),(x+1,y-2)]
    for i in L:
        for j in i:
            if not (1<=j<=8):
                L.remove(i)
                break
    return L

x,y = map(int, input("Enter 2 coordinates (1 to 8) for initial position of knight on the chessboard separated by a space: ").split())
xf,yf = map(int, input("Enter 2 coordinates (1 to 8) for final destination of knight on the chessboard separated by a space: ").split())

if (xf, yf) in GenMoves(x,y):
    print("Knight's tour is possible in ONE MOVE ONLY!")
else:
    for i,j in GenMoves(x,y):
        if (xf, yf) in GenMoves(i,j):
            print("Knight's tour is possible in TWO MOVES!")
            break
    else:
        print("Knight's tour is not possible")
