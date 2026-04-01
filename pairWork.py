print()
n= input("Enter your name: ")
m1=float(input("Marks of module 1: "))
m2=float(input("Marks of module 2: "))
m3=float(input("Marks of module 3: "))
m4=float(input("Marks of module 4: "))
a= float(input("Enter the number of classes attended(96): "))
att=(a/96)*100
average = (m1+m2+m3+m4)/4
if (m1>100 or m2>100 or m3>100 or m4>100):
    print("Wrong marks have been entered! please recheck the marks and try again.")
    print()
    quit()
else:
    pass
print()
avg = (m1+m2+m3+m4)/4
print("Average: ",avg, "%")
if 100>avg>=80:
    print("Grade: A")
elif 100>avg>=60:
    print("Grade: B")
elif 100>avg>=40:
    print("Grade: C")
elif avg>100:
    print("Grade: Error! Recheck the marks entered!")
else:
    print("Grade: D")
print("Attendance:%.2f"%att,"%")
if (100>=avg>=40 and 100>=m1>=40 and 100>=m2>=40 and 100>=m3>=40 and 100>=m4>=40 and 100>=att>=90):
    print("Status: Pass")
else:
    print("Status: Fail")
if (100>=avg>=80 and 100>=att>=90):
    print("Eligible for reward.")
else:
    print("Not eligible for reward.")
print()