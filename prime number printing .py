range_start=int(input("Enter the start of the range:"))
end_range=int(input("Enter the end of the range:"))
c1=0;
for num in range(range_start,end_range+1):
    c2=0;
    for number in range(1,num+1):
        if num%number==0:
            c2=c2+1
    if c2==2:
        print(num)




