mark = int(input("Enter your Mark : "))
if(mark<35):
    print("Poor student")
elif(mark>35 and mark<=70):
    print("Average student")
elif(mark>70 and mark<100):
    print("Good student")
else:
    print("Invalid mark")
    
