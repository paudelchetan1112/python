a="chetan"
print(len(a))
text="the quick clever brown fox jumps over the lazy dog"
print(len(text))
print(" ".join(a))


fruits=["apple","banana","mango","orange"]
new_string=",".join(fruits)
myname="Banke Bageshwari Campus"
print("orginal Name:",myname)
print("Updated name:",myname.replace("Campus","college"))

print(myname.split())



bbc="Banke Bageshwari"
print(bbc[6])
print(bbc[-16])

# Accessing a range of index 

print(bbc[6:15])
print(bbc[0:5])

# specifying stride whiole slicing string

print(bbc[4:15:2])
 
 # count method certain letter or string

print(bbc.lower().count("b"))
page_name="Banke Bageshwori Campus Nepalgunj Banke"
print(page_name.count("Banke"))




