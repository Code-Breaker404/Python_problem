subject =["c","java","Python","css","html"]
print(subject)
print(subject[0])
print(subject[3])
print(subject[2:])
print(subject[-1])
print("Java" in subject) #case sansitive;
print("c" in subject)
print("pandas" not in subject) # Not statement ar use 
print(subject + [999,"pandas"])
print(len(subject))
subject.insert(2,"OS")
print(subject)
print(len(subject))
subject.sort()
print(subject)
subject1=subject.copy()
print(subject1)  