Names=[]
Ages=[]
CGPA=[]
Outputs=[]
for i in range(2):
    name=input("enter the name")
    age=int(input("enter the age"))
    cgpa=float(input("enter the CGPA"))
    output=input("enter the true od false")

    Names.append(name)
    Ages.append(age) 
    CGPA.append(cgpa)
    Outputs.append(output)
    
print("Name",Names)
print("Ages",Ages)
print("CGPA",CGPA)
print(bool("Output",Outputs)
