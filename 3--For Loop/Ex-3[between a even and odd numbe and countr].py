a=int(input("Enter a value: "))
b=int(input("Enter b value: "))

print("Even number between ",a,"to",b)
Even_count=0

for i in range(a,b):
    if(i%2==0):  
        print(i)
        Even_count=Even_count+1
        
print("Number of Even Count =",Even_count)

print("Odd number between of ",a,"to",b)
odd_count=0

for i in range(a,b):
    if(i%2!=0):  
        print(i)
        odd_count=odd_count+1
        
print("Number of Count Odd =",odd_count)
