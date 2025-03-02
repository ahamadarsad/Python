a=[]
print("Enter  student marks : ")
for i in range(1,6):
    mark=int(input("Enter student mark "+str(i)+": "))
    a.append(mark)
print("Student mark of : ",a)

sum= 0
for i in a:
    sum=sum+i
print("sum of mark",sum)
avg= sum/5
print("Average of  :",avg)


