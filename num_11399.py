N = int(input())
P = list(map(int, input().split()))

P.sort()


def allMin(N, P) :
    sumMin = 0
    time = 0
    
    for i in range(N):
        sumMin += time + P[i]
        time += P[i]
        
    return sumMin

print(allMin(N, P))