p={6,28,496,8128,33550336}
print(p)
s=set([2,4,16,64])
print(s)

#for-loop
for x in {1,2,4,8,16,32}:
    print(x)
q={2,9,6,4}

print(3 in q)
print(3 not in q)

#adding an object to a set
k={81,1039}
k.add(85)
k.add(12)


#adding multiple objects
k.update([37,128,97])


#methods of removing objects
k.remove(97)
k.discard(98)    #preffered

#Set algebra
blue_eyes = {"Olivia","Harry","Lily","Jack","Amelia"}
blonde_hair = {"Harry","Jack","Amelia","Mia","Joshua"}
smell_hcn = {"Harry","Amelia"}
taste_ptc={"Harry","Lily","Amelia","Lola"}
o_blood={"Mia","Joshua","Lily","Olivia"}
a_blood={"Harry"}
b_blood={"Amelia","Jack"}
ab_blood={"Joshua","Lola"}

print(blue_eyes.union(blonde_hair))
print(blue_eyes.intersection(blonde_hair))
print(blonde_hair.difference(blue_eyes))
print(blonde_hair.symmetric_difference(blue_eyes))
print(smell_hcn.issubset(blonde_hair))
print(taste_ptc.issuperset(smell_hcn))
print(a_blood.isdisjoint(o_blood))