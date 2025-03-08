s="abc898df9lgkres,abc8989,343,wqrwc,3453"

list = s.split(",")
# ['abc898df9lgkres',abc898, '343', 'wqrwc', '3453']
print(list)
# print(list[1])
sum =0
for i in range (0,len(list) ): # 0,1, 2,3, 4
    r= list[i] #'3453'
    if (r.isdigit()==True):
        print(r)
        sum=sum + int(r)
    elif (r.isalpha()==True):
        pass;
    elif(r.isalnum()==True):

        #     case 2   alpha nummber can appear randomly
        num = ""
        for j in range(0, len(r)):

            if (r[j:j + 1].isdigit() == True):
                # print(num," -- ")
                num =num + r[j:j + 1]

            else:
                pass

        print(num)
        sum = sum +int(num)



        #     case 1    when alphabets cannot appear after digits

        # for j in range(0, len(r)): # string "abc8989" j = 3
        #     if(r[j:j+1].isdigit()==False):
        #         pass
        #     else:
        #         print(r[j:])
        #         sum = sum + int(r[j:])
        #         break;

print(sum)



# 8989+343+3453

# print(s.center(20," "))
# l= len(s)
# l= l//2
# print(s[l:l+1])

# print(s.center(10,"="))

# s.isnumeric()
# s.isdigit()
# s.isdecimal()
# s.isdigit()
# print(s.isalnum())
# print(s.isdigit())
# s = "abcd efghij"
    #0123456789
    #-10 , -9 .........-1
    #  left to right
    # step negative = > right to left
# r= s[6:1:-1]


# print(r)
# output =  "gfedc"
# slicing
# r = s[4:10:3]
# r= s[-3::-2]
# first index => include
# second index => excluded index

# print("original string : " , s)
# print("sliced string : ",r)
