

# def login():
#     name=str(input("Enter Username:"))
#     password=str(input("Enter password:"))
#     if(name=='admin' and password=="admin123"):
#         print("Login Successful")
#     else:
#         print("nikal")

# print(login())
# def add_numbers(x,y,z):
#     a=x+y+z
#     b=x+y
#     c=y+z
#     print(a,b,c)

# print(add_numbers(5,4,2))

def profile_info(username, followers):
    print(f"Username:{username}")
    print(f"Followers:{followers}")

profile_info('user1',1500)
profile_info(followers=2500, username="user2")
