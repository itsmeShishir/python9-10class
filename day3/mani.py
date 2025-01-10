# data structure
# -> list, set, dict, truple
#list -> 
a = [1,2,3,4,5,6, "shishir", True]
print(len(a))
print(a[6])
a.append(False)
print(a)
a.remove(1)
print(a)
a.pop()
print(a)

# list comprehension
b = [x**3 for x in range(0,10)]
print(b)

# truple -> data type
# immutable data type 
c = (1,2,3)
print(c)
print(c[0])

# dict -> data type
d = {
    "name":"shishir bhandari",
    2: 27,
    "ismale": True
}
print(d)
print(d["name"])
print(d[2])
print(d.values())
print(d.keys())
print(d.items())

print("here comes for loop")
for keys in d:
    print(keys)

#set -> data dype with correct order
unique = {1,2,3,4}
print(unique)
unique.add(5)
print(unique)
unique.add(5)
print(unique)
unique.remove(5)
print(unique)
# intersection and union
set2 = {4,5,6,7}
set1 = set2.intersection(unique)
print(set1)
set1 = set2.union(unique)
print(set1)

#function -> a block of code which will run when we call it 
# and it may contain some -> parameters

# basic funtion define 
def yourName():
    print("my name is shishir bhandari")

yourName()
yourName()
yourName()

#how to use parameter in function
def youNames(name):
    print("my name is ", name)
youNames("Shishir")
youNames("Hari")
youNames("Sita")



