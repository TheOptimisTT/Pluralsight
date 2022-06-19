t=("Norway",4.953,3)
print(t)
print(t[0])
print(t[2])

print(f"The len(t) is: {len(t)}")

for item in t:
    print(item)

t+=(338186.0,265e9)
print(t)

a=((220,284),(1184,1210),(2620,2924),(5020,5564),(6232,6368))
print("a=",a)
print("a[2][1]=",a[2][1])

k=(391,)  #k=(391) is an int
print(type(k),k)
 
e=() #empty tuple

p= 1,1,1,4,6,19
print(type (p),p)

def minmax(items):
    return  min(items), max(items)
print(minmax([83,33,84,32,85,31,86]))

lower,upper=minmax([83,33,84,32,85,31,86]) #tupple unpacking
print(f"lower is {lower}, upper is {upper}")

(a,(b,(c,d)))=(4,(3,(2,1))) #unpacking nested tuple
print(a)
print(b)
print(c)
print(d)

#swapping two or more variables
a="Jelly"
b="Bean"
print(f"a is {a}, b is {b}")
a,b=b,a
print(f"a is {a}, b is {b}")

#tuple from an excisting collection
print(tuple([561,1105,1729,2465]))
print(tuple("Carmichael"))

#Test for containment
print(5 in (3,5,17,257,65537))
print(5 not in (3,5,17,257,65537))
print(5 in (3,17,257,65537))