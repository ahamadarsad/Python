a=int(input("Enter a value: "))
b=int(input("Enter b value: "))

print("Even number between ",a,"to",b)
E_count=0

for i in range(a,b):
    if(i%2==0):  
        print(i)
        E_count=E_count+1
        
print("Number of Even Count =",E_count)

print("Odd number between of ",a,"to",b)
o_count=0

for i in range(a,b):
    if(i%2!=0):  
        print(i)
        o_count=o_count+1
        
print("Number of Count Odd =",o_count)
