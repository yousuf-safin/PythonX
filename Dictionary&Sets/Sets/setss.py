s={1,2,3,45,"Hamza"} #set
print(s,type(s))
s.add(69)
print(s)
s.remove("Hamza")
print(s)
e= set(s) #empty set
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))

R1 = s1-s2
print(R1)