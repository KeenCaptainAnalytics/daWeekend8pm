# sum of even elements


# sum of all the values at even indices
# (14, 45, 67, 78, 89, 21) => elements of tuple
#  0   1    2   3  4   5 => index


def sumEven(*a):
    l = len(a)  #=> 9
    sum =0
    for i in range (0, l, 2):
        sum= a[i] +sum  # i =8+2 = 10  , sum =52+8 = 60

    print(a , sum)


sumEven(12, 14, 16, 18, 20, 2, 4,6,8)
            # 0   1   2   3   4   5  6 7 8 => index



# def add(*tup) :
#     l=  len(tup)
#     sum =0
#     for i in range (0, l):
#         sum= sum + tup[i] # i =0 , sum =  0 + 12 = 12 , 2nd i=1 sum = 12 + 13 = 25 , i =2 sum = 25 + 14 =39 i =3
#
#     print(tup, sum)
#
# add(12,13,14)
# add(12, 45)
# add(14,45,67,78,89,21)
