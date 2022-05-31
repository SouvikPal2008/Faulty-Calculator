# 45 + 3 = 555 , 56 + 9 = 77 , 56 / 6 = 4
print("Welcome to Apna Calculator")
print("Operators" , "--> + , - , / , *")
print("Please Enter Your Operator")
operator = input()
print("Please Enter Your First Number")
Num1 = int(input())
print("Please Enter Your Second Number")
Num2 = int(input())
if operator == '+' and Num1 == 45 and Num2 == 3:
    print("Your Answer is" , "555")
elif operator == '+' and Num1 == 56 and Num2 == 9:
    print("Your Answer is" , "77")
elif operator == '/' and Num1 == 56 and Num2 == 6:
    print("Your Answer is", 4)
else:
    print("Sorry But Do You want to Add" , "If Yes Then 1 if Not Then 0")
    sorry1 = int(input())
    if sorry1 == 1 :
        print("Your Answer is" , Num1 + Num2)
    else:
        print("Do You Want To Substract", "If Yes Then 1 if Not Then 0")
        sorry2 = int(input())
        if sorry2 == 1 :
            print("Your Answer is" , Num1 - Num2)
        else:
            print("Do You Want To Multiply", "If Yes Then 1 if Not Then 0")
            sorry3 = int(input())
            if sorry3 == 1 :
                print("Your Answer is" , Num1 * Num2)
            else:
                print("Do You Want To Devide", "If Yes Then 1 if Not Then 0")
                Sorry4 = int(input())
                if Sorry4 == 1 :
                    print("Your Answer is" , Num1 / Num2)
                else:
                    print("Sorry We Can;t Help You Please ReRun The Program")