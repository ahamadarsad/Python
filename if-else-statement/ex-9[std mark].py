m1=int(input("Enter Mark 1 :"))
m2=int(input("Enter Mark 2 :"))
m3=int(input("Enter Mark 3 :"))
m4=int(input("Enter Mark 4 :"))
m5=int(input("Enter Mark 5 :"))
total =m1+m2+m3+m4+m5
print(total)
avg =total/5
print(avg)
if(avg>=35):
    print("You good to Go")
else:
    print("Additional calss is required")
