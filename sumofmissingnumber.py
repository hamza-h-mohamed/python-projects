def sum_of_missing_number(array):
    mx=max(array)
    mn=min(array)
    newlist = []
    for i in range(mn,mx):
        if mn not in array:
            newlist.append(mn)
        mn+=1
    print(newlist)
    print(sum(newlist))

a = ([12,15,16,11,17,20,27])
sum_of_missing_number(a)