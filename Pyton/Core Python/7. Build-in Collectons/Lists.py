# Negative indices
r=[1,-4,10,-16,15]
print(r[-1])
print(r[-2])
#-0 and 0 are the same element
print(r[-0])
print(r[0])

# Slicing
s=[3,186,4431,74400,1048443]
print(s)
print(s[1:3])
print(s[1:-1])
print(s[2:])
print(s[:2])
print(s[:])

#Copying a list

t=s
print(t is s) #not a copy

r=s[:]
print(r is s) #Copy but only references are copied.

#Only References are Copied
#Fuction to copy str.copy()
u=s.copy()
print(u is s) #Copy but only references are copied.

#copy via list. Prefered way
v=list(s)
print(v is s)
print()

#Shallow copying is basically this
a=[[1,2],[3,4]]


b=a[:]  #standart list copy
print(f"a= {a}")
print(f"b= {b}")
print(f"a is b {a is b}")
print(f"a == b {a == b}")
print(f"a[0]={a[0]}")
print(f"b[0]={b[0]}")
print(f"a[0] is b[0] {a[0] is b[0]}")

a[0]=[8,9]
print(f"a[0]={a[0]}")
print(f"b[0]={b[0]}")
print(f"a[0] is b[0] {a[0] is b[0]}")

a[1].append(5)
print(f"a={a}")
print(f"b={b}")
print()

#Lists support repetition
c=[21,37]
d=c*4
print(c)
print(d)
print()

#Repetition will copy the reference
s=[[-1,1]]*5
print(s)
s[2].append(7)
print(s)

#list.index()

w="the quick brown fox jumps over the lazy dog".split()
print(w)
i=w.index("fox")
print(f"w.index(fox) is: {i}")
print(f"w[i] is: {w[i]}")
print(f"usese of the {w.count('the')}")

print(37 in [1,78,9,37,34,53])
print(78 not in [1,78,9,37,34,53])

#Remove an elemet form a list .del .remove
u="Jackdaws love my big sphinx of quartz".split()
print(u)
del u[3]
print(u)
u.remove("Jackdaws")
print(u)
print()

#list.incert()
a="I accidentally the whole univerce!".split()
a.insert(2, "destroyed")
print(a)
print(' '.join(a))
print()

#Concatenating lists

m=[2,1,3]
n=[4,7,11]
k=m+n
print(k)

k+=[18,29,47]
print(k)

k.extend([76,129,199])
print(k)
print()

#list.reverce() and list.sort()
g=[1,11,21]
print(g)
g.reverse()
print(g)

d=[17,41,1,29]
print(d)
d.sort()
print(d)

print()

#Key parameter to list.sort()
h="not perplexing do tandwriting family where I illegibly know doctors".split()
h.sort(key=len)
print(" ".join(h))
print()

#Reversing and sorting into copies
x=[4,9,2,1]
y=sorted(x)
print(y)
print(x)

p=[9,3,1,0]
q=reversed(p)
print(q)
print(list(q))
