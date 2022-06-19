#Basic range usage 
print(range(5))
print(range(5,10))

#Creating quick counters
for i in range(5):
    print(i)

#call to the list
print(list(range(5,10)))
print(list(range(10,15)))

#range supports a "step argument" range(start,stop,step)
print(list(range(0,10,2)))

#Proper way of printing a list
s=[0,1,4,6,13]
for v in s:
    print(v)

#enumerate()
t=[6,372,8862,148800,2096886]
for p in enumerate(t):
    print(p)

#tuple umpacking + enumerate
for i,v in enumerate(t):
    print(f"i={i}, v={v}")