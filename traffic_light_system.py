do:
light=input("Enter traffic Light color(red/yellow/green):")
if light.lower()=="red":
    print("Stop")
elif light.lower()=="yellow":
    print("drive Slowly")
elif light.lower()=="green":
    print("Go")
else:
    print("Invalid Color")
    while (light.lower()=="red")