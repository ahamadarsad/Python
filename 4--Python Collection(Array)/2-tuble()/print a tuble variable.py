# tuble called by -- > ()
print("print a Tuble: ",end="")
a=(0,10,20,30,40,50)
print(a)
print()
print(type(a))
print()

#tuble cannot modify tha value. so, tuble type variable change to list
print("Change tuble to list: ",end="")
b=list(a)
print(b)

print()

print("add a value: ",end="")
b.append(60)
print(b)

print()

print("Remove a value: ",end="")
b.pop(0)
print(b)

print()

print("print a one value: ",end="")
print(a[1])

