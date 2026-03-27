print()
n= input("Enter your name: ")
m1=float(input("Marks of module 1: "))
m2=float(input("Marks of module 2: "))
m3=float(input("Marks of module 3: "))
m4=float(input("Marks of module 4: "))
a= float(input("Enter the number of classes attended: "))
att=(a/96)*100
print()
avg = (m1+m2+m3+m4)/4
print("Average: ",avg, "%")
if avg>=80:
    print("Grade: A")
elif avg>=60:
    print("Grade: B")
elif avg>=40:
    print("Grade: C")
else:
    print("Grade: D")
print("Attendance: ",att,"%")
if (avg>=40 and m1>=40 and m2>=40 and m3>=40 and m4>=40 and att>=90):
    print("Status: Pass")
else:
    print("Status: Fail")
if (100>=avg>=80 and 100>=att>=90):
    print("Eligible for reward.")
else:
    print("Not eligible for reward.")
print()