n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end='')
    for j in range(2*(n-1)):
        print("",end=""):
    for j in range(i):
        print()        


        if (i==0 or i==n-1 or j==0 or j==n-1):
            print('*',end='')
        elif(i==j or i+j==n-1):
            print('*', end='')
        else:
            print(' ',end=''):
    print()                  
