# map(func, iterl)

def square(x):
    return(x*x)

num=[1,2,3,4,5]
result=list (map(square,num))
print(result)

#filter /remove kore ;
result=list(filter(lambda x: x%2==0,result))
print(result)