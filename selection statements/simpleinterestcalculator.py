#program to calculate simple interest
#input of principal from user
principal=float(input("Enter principal (in Rs): "))
#validating principal
if principal<=0:
    exit("Error: Principal should be greater than 0")
#input of rate of interest from user
rate=float(input("Enter rate of interest (in %): "))
#validating rate of interest
if rate<=0:
    exit("Error: Rate of interest should be greater than 0")    
#input of time from user
time=int(input("Enter time (in years): "))
#validating time
if time<=0:
    exit("Error: Time should be greater than 0")
#Displaying data
print("---------------------------------")
print("Principal :Rs ",principal)
print("Rate of interest : ",rate,"%")
print("Time : ",time," years")
#Displaying Simple Interest
print("Simple Interest : Rs ",(principal*rate*time)/100)
'''Output:
Enter principal (in Rs): 10000
Enter rate of interest (in %): 5    
Enter time (in years): 3
---------------------------------
Principal :Rs  10000.0
Rate of interest :  5.0 %
Time :  3  years
Simple Interest : Rs  1500.0
'''