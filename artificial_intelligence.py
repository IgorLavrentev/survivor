def SumOfThe(N, data):
    summ = 0 # variable for the sum of all numbers except the next one
    for j in range(N):
        x = data.pop(0) # variable for the next item in the list    
        for j in range(len(data)):
            summ += data[j]
        if summ == x: # comparing the next item with the sum of the remaining items in the list
            return x
        else:
            summ = 0
            data.append(x)
