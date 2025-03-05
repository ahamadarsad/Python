# (a+b)*c using two functions

a=int(input("Enter A value : "))
b=int(input("Enter B value : "))
c=int(input("Enter c value : "))

#function 1
def add(num1,num2):
    total = num1 + num2
    return(total)

#function 2
def multiplay(add,mulvalue):
    result= add * mulvalue
    return(result)

# first function call 
addition = add(a,b)

#second function call
mul = multiplay(addition,c)
print(mul)
