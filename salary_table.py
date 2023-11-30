def SynchronizingTables(N, ids, salary):
    dictionary = {}
    salary.sort() # sorting the salary array

    # matching account numbers and salaries using a dictionary
    i = 0
    for j in range(min(ids), max(ids) + 1):
        if j in ids:
            dictionary[j] = salary[i]
            i += 1

    salary.clear() # deleting the contents of the salary array

    # filling in the salary list according to the accounting numbers
    for k in ids:
        salary.append(dictionary[k])

    return salary
    