n=input("Enter a test of number :")   #10,20,30,...
list=n.split()
print(list);
sum=0
for num in list :
    sum=sum+int(num)
print(sum);