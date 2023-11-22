def squirrel(N):
    if N == 0:
        return 1
    for i in range(1, N):
        N = N * i
    return N // pow(10, len(str(N)) - 1)