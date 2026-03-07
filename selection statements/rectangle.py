#program to calculate perimeter and area of rectangle
#input of length from user
length=float(input("Enter length of rectangle(in cm) : "))
#validate length
if length<=0:
    exit("Error: Length should be greater than 0")
#input of width from user
breadth=float(input("Enter breadth of rectangle(in cm) : "))
#validate breadth
if breadth<=0:
    exit("Error: Breadth should be greater than 0") 
#--------------------------------------------------------
#Displaying data to the user
print("---------------------------------")
print("------ Rectangle ------")
print("Length : ",length," cm")
print("Breadth : ",breadth," cm")
#Displaying perimeter and area of rectangle
print("Perimeter : ",2*(length+breadth)," cm")  
print("Area : ",length*breadth," sq. cm")
#--------------------------------------------------------
'''Output:
Enter length of rectangle(in cm) : 5
Enter breadth of rectangle(in cm) : 3   
---------------------------------
------ Rectangle ------
Length :  5.0  cm
Breadth :  3.0  cm
Perimeter :  16.0  cm
Area :  15.0  sq. cm
'''