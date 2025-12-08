user={'username':'user123', 'online':True, 'follower':987}
print("UserName:",user['username'])


for key, value in user.items():
    print(f"{key}:{value}")

print(user.keys()) # print all keys
print(user.values()) #print all value of key


student_data={"username":"student1", "age":21}
#adding new key value pair
student_data["address"]="npj"


#update key value 
print(student_data)
user.update({'online':False, 'followers':1000})
print(user)

# delete key value
del user['online']
print(user)

#to clear dictionary
user.clear()
print(user)



