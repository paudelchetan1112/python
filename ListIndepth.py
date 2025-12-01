mixed_data=[1,"apple",3.5,True]
mixed_data[0]="Banana"
print(mixed_data)

#slicing list
Fruits=["apple", "banana", "orange","kiwi", "mango"]
print(Fruits[0:3])

#Modifying Lists with Operators
fruit1=["Apple","banana","cherry", "mango"]
vegetables=["Couliflower", "Cabbage","Carrot", "Potato"]
all_item=fruit1+vegetables;
print(all_item)
#astrick operator
print(fruit1*2)
print(vegetables*3)
#removing an Item form list
del fruit1[1]
print(fruit1)
#removing an Item by give a range
del fruit1[1:3]
print(fruit1)