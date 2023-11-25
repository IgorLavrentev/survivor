def ConquestCampaign(N, M, L, battalion):

    field = [] # creating an array "Field"
    count = 0 # counter of landing of paratroopers

    # field formation
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            field.append(i)
            field.append(j)

    # deleting the first polygons
    for p in range(0, L + 1, 2):
        for e in range(0, len(field) - 1, 2):
            if field[e] == battalion[p] and field[e + 1] == battalion[p + 1]:
                del field[e:e+2]
                break
    count += 1

    while field != []:
        # generating a list of the following captured polygons
        for s in range(0, len(battalion), 2):

            battalion.append(battalion[s] + 1)
            battalion.append(battalion[s + 1])
            battalion.append(battalion[s] - 1)
            battalion.append(battalion[s + 1])

            battalion.append(battalion[s])
            battalion.append(battalion[s + 1] + 1)
            battalion.append(battalion[s])
            battalion.append(battalion[s + 1] - 1)

        # deleting regular polygons
        for r in range(0, len(battalion), 2):
            for k in range(0, len(field) - 1, 2):
                if field[k] == battalion[r] and field[k + 1] == battalion[r + 1]:
                    del field[k:k+2]
                    break
        count += 1

    # output of the result (number of days)
    return count
