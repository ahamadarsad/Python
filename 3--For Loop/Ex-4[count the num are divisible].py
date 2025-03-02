a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 :"))
count=0
for i in range(a,b):
    if(i%3==0 and i%5==0):
        print(i)
        count=count+1
print(a," and ",b,"count of :",count)
 
