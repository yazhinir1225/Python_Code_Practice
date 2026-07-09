Names=[]
Ages=[]
CGPAs=[]
Cities=[]
for i in range(3):
    name=input("Enter Name")
    Age=int(input("Enter Age:"))
    cgpa=float(input("Enter CGPA:"))
    city=input("Enter City:")
    Names.append(name)
    Ages.append(Age)
    CGPAs.append(cgpa)
    Cities.append(city)


print(Names)
print(Ages)
print(CGPAs)
print(Cities)

for name in Names:
    print(name.upper())
for city in Cities:
print(city.lower())

if cgpa>7.5:
    print(name,"Elegoble for placement")
else:
    print(name,"Not eligible for placement")    


#for cities in range("Chennai"):
if Cities in "Chennai":
    print("Chennai Found")
else:
    print("Chennai Not Found")    