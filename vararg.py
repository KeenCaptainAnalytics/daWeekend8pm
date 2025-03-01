# target = 9,
# call(9, 1, 3, 5, 7, 4, 2)
# output => 5 and 4

def fn(target, *a):

    for i in range (0, len(a)):
        #  i = 0, 1, 2
        first = a [i] # 5
        second = target - first # 4
      
        for j in range( i+ 1, len(a)):
            # j  3. 4
            if( second == a[j]):
                print( first , second )
                return
            else:
                pass

fn(9, 1, 3, 5, 7, 4, 2)
                # 0  1 2   3  4  5
    # print(target,"target")
    # print(a)




# sum ele => 3 5 7

# def sumEle(*a):
#     sum =0;
#     for i in range (0, len(a)):
#         if(a[i]%3==0 and a[i]%5 ==0  and a[i]%7 ==0):
#             sum = sum+ a[i]
#         else:
#             pass
#     print(a, sum)
#
# sumEle(105, 67, 34, 90 ,210)

# sum of even elements

# def sumEle(*a):
#     sum = 0
#     for i in range (0, len(a)):
#         if(a[i]%2==0):
#             sum = sum + a[i]
#         else:
#             pass
#
#     print(a, sum)
#
# sumEle(12, 34, 6, 9 , 7, 71);

# sum of all the values at even indices
# (14, 45, 67, 78, 89, 21) => elements of tuple
#  0   1    2   3  4   5 => index


# def sumEven(*a):
#     l = len(a)  #=> 9
#     sum =0
#     for i in range (0, l, 2):
#         sum= a[i] +sum  # i =8+2 = 10  , sum =52+8 = 60
#
#     print(a , sum)
#

# approach 2
# def sumEven(*a):
#     l = len(a)  #=> 9
#     sum =0
#     for i in range (0, l):
#         if(i%2==0):
#             sum= a[i] +sum  # i =8+2 = 10  , sum =52+8 = 60
#
#     print(a , sum)
#
#
# sumEven(12, 14, 16, 18, 20, 2, 4,6,8)
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
