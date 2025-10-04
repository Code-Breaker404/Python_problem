# 1+2+3+4+5+......+n;
n=int(input("Enter the last number :"))
sum=0
#for x in range(1,n+1,1):
for x in range(1,n+1,2):
    sum=sum+x
print("The result is ",sum)  
