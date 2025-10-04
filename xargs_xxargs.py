#xargs 

def student(*details):
    print(details)

student(23,"Mustakin",3.75)   
def add(*numbers) :
    sum=0
    for num in numbers :
        sum=sum+num
    print(sum)

add(23,56)
add(50,75,25)


#xxargs
def student(**details):
    print(details)

student(id=23,name="Mustakin")  
 


