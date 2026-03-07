#program to input time in seconds and convert it into hours, minutes and seconds    
#taking input from user
second=int(input("Enter time in seconds : "))
#initialize hour and minute as 0
hour=0
minute=0
#calculating number of hors in given seconds
if second>=3600:
    hour=second//3600
    second=second%3600
#calculating number of minutes in remaining seconds
if second>=60:
    minute=second//60
    second=second%60
#printing the result
print("Time : ",hour," Hour",minute,"minute",second," second")
#----------------------------------------------------------
'''Output:
Enter time in seconds : 3945
Time :  1  Hour 5 minute 45  second
'''