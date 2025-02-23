# calculator => addition, sub, duv, multi

def calculator(num1=0, num2=0, op="+"):
    result =0
    if (op=='+'):
        result = num1+num2
    elif (op=="-"):
        result = num1-num2
    elif (op == "*"):
        result = num1*num2
    elif (op=="/"):
        result = num1/num2
    else:
        result = 0;

    return result;

ch = "y"
number1 = int(input("enter a number : "))
number2 = int(input("enter second number : "))

while ch == "y":
    op= input("enter the input operator : ")
    finalResult = calculator(number1, number2, op);
    number1 = number2
    number2 = finalResult

    print(finalResult)
    ch = input("Do you want to continue(y/n) : ")

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
