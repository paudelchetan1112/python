# a="chetan"
# number=123
# print(type(number))
# print(type(123))
string="57"
float=float(string)
integer=int(string)
print(type(float))
print(type(integer))
stringagain=str(float)
a="34"
b="56"
result=int(a)-int(b)
print(result)
# Converting to Tuples and Lists
Fruits=["Banana", "Orange", "Mango"]

print(tuple(Fruits))


# Using Formatter with single PlaceHolder
print("Iam {} year old.".format(25))
college_name="Banke Bageshwari Campus"
address="Nepalgunj Banke"
print("MY college Name is {}".format(college_name))


# Mulitple Place Holder
print("My college name is {} and it is located in {}".format(college_name, address))

 # formatter with Index

#  print("My college name is {1} and it is located in {0}".format(college_name, address))


product="smartPhone"
price="689.99999"
quantity=3450
print(f"ProductName:{product},\nProductPrice:Rs{price},\nQuantity:{quantity}")
