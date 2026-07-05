#creating List for all
Names=[]
Ages=[]
CGPAS=[]
Citys=[]

for i in range(2):
    #getting input from user
    Name=input("Enter the name")
    Age=int(input("enter the Age"))
    Cgpa=float(input("Enter the CGPA"))
    City=input("Enter the city")
    Names.append(Name)
    Ages.append(Age)

#Printing the value
print(Name)
print(Age)
print(Cgpa)
print(City)

# converting into uppercase
print(Name.upper())
print(Age.upper())
print(Cgpa.upper())
print(City.upper())