user={'username':'user123', 'online':True, 'follower':987}
print("UserName:",user['username'])


for key, value in user.items():
    print(f"{key}:{value}")

print(user.keys()) # print all keys
print(user.values()) #print all value of key
