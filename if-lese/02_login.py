username = "admin"
password = "123456"

user_input = str(input("Enter your Username : "))
pass_input = complex(input("Enter your Password : "))

if user_input == "admin" and pass_input == "123456":
    print("Login Success !!!")
else:
    print("Invalid Username or Password")   