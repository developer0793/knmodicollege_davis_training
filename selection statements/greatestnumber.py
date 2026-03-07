#program to find out the greatest number among five numbers
#taking input from user
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))
num4=int(input("Enter fourth number : "))
num5=int(input("Enter fifth number : "))
#finding greatest number
if(num1 == num2 == num3 == num4 == num5):
    print("All numbers are equal")
elif(num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5):
    print(num1," is greatest number")
elif(num2 >= num3 and num2 >= num4 and num2 >= num5):
    print(num2," is greatest number")
elif(num3 >= num4 and num3 >= num5):
    print(num3," is greatest number")
elif(num4 >= num5):
    print(num4," is greatest number")
else:
    print(num5," is greatest number")
'''Output:
Enter first number : 10
Enter second number : 20
Enter third number : 15
Enter fourth number : 5
Enter fifth number : 25
25  is greatest number
'''
