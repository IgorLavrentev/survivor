def MadMax(N, Tele):
# sorting the array in ascending order
    Tele.sort()

    s = (len(Tele)//2) # middle
    Tele_start = Tele[0:s] # the first part of the list
    Tele_end = Tele[s: len(Tele)-1] # the second part of the list
    Tele_end.sort(reverse=True) # the second part of the list is in reverse order

    new_list = Tele_start + [max(Tele)] + Tele_end # "assembling" the final list

    # output of the resulting list
    return new_list
