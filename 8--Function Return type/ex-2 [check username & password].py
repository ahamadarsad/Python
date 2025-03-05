User_name = "Arsad"
Password = "2.11.204"

def check(u_name,password):
    if(User_name==u_name and Password==password):
        return("User_name and password is correct")
    else:
        return("User_name and password is not correct")

name = input("Enter user_name :")
passw = input("Enter password :")
print()
print(check(name,passw))
