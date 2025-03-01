a=[]
print("Enter 10 numbers")
for i in range(1,11):
    user=int(input("Enter number "+str(i)+": "))
    a.append(user)
print(a)

sum= 0
for i in a:
    sum=sum+i
print("sum of",sum)
avg= sum/5
print("Average of :",avg)


