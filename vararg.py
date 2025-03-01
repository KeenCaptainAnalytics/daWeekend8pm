def add(*tup) :
    l=  len(tup)
    sum =0
    for i in range (0, l):
        sum= sum + tup[i]

    print(tup, sum)



    # print(tup)
    # print(len(tup))

add(12,13,14)
add(12, 45)
add(14,45,67,78,89,21)
