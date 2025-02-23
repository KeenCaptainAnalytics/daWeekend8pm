def addstring(*s):
    result =""
    for i in range (0, len(s)):
        result = result +"->"+ s[i]

    print(result)


addstring("lily", "rose" )
addstring("rose", "sunflower", "lily")
addstring("rose")


# st1 = 90
# st2 = 80
# st3= 70
# st = (50, 56, 57)
# print(st[0])
# print(st[1])
# print(st[2])
# num = (1,2,3,4)

# var-arg(variable arguments)
# def sumNum(*num):
#
#     print(sum(num))

    # print(num)
    # print(type(num))

# sumNum(1,2,3)
# sumNum(1)
# sumNum(1,4,8,9,3)
# sumNum()




#implement a function which takes in the number input
# and gives the output string as "even" or "odd"

# def isEven(num ):
#     if(num %2==0):
#         return "even"
#     else:
#         return "odd"
#
# str = isEven(787)
# print(str)

# calculator => addition, sub, duv, multi


# def calculator(num1=0, num2=0, op="+"):
#     result =0
#     if (op=='+'):
#         result = num1+num2
#     elif (op=="-"):
#         result = num1-num2
#     elif (op == "*"):
#         result = num1*num2
#     elif (op=="/"):
#         result = num1/num2
#     else:
#         result = 0;
#
#     return result;
#
# # calculator(78, 89, "+")
#
# ch = "y"
# number1 = int(input("enter a number : "))
# number2 = int(input("enter second number : "))
#
# while ch == "y":
#     op= input("enter the input operator : ")
#     finalResult = calculator(number1, number2, op);
#     number1 = number2
#     number2 = finalResult
#
#     print(finalResult)
#     ch = input("Do you want to continue(y/n) : ")

# fibo => 0 , 1 , 1, 2, 3, 5, 8, 13......
# 0 1 => + => 1
# 1 1 => + => 2
# 1 2 => + => 3
# 2 3 => + => 5
# 3 5 => + => 8
# 5 8 => + => 13



# print(calculator(78, 98,"-"))
# print(calculator(778, 65,"*"))
# print(calculator(778, 65,"+"))
