import math
def TheaterSquare(n,m,a):
    #print(math.floor((n*m)/2))
    return 2*math.floor((n*m)/pow(2,a))

n,m,a= list(map(int, input().split()))
# print(TheaterSquare(n,m,a))
TheaterSquare(6,6,4)