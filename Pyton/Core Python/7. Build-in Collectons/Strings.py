#the len function
print(len("The capital of Bulgaria is Sofia"))

# +
print("New"+"found"+"land")

# +=
s="New"
s+="found"
s+="land"
print(s)

#the str.join() funciton
colors=";".join(["1","2","3"])
print(colors)
print("".join(["high","way","man"]))

# str.partition()
print("unforgetable".partition("forget"))
print(type("unforgetable".partition("forget"))) #returns a tuple

departure,separator,arrival="London:Edinburg".partition(':')
print(departure)
print(separator) # usuallly we don't need this value and we use _
print(arrival)

#string formating
print("{0} deg north, {1} deg east.".format(59.7,10.4))
print("the age of {0} is {1}.".format("Jim",32))
print("The age of {0} is {1}. {0}'s birthday is {2}.".format("Jim",24,"Octovber 31th"))
print("Reticulating spline {} of {}.".format(4,23))
print("Current position {latitude} {longitute}.".format(latitude="60N",longitute="5E"))
print("Galactic position x= {pos[0]}, y= {pos[1]}, z= {pos[2]}".format(pos=(62.2,23.1,82.2)))

import math
print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
# :.3f
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

value = 4*20
print("The value is {value}".format(value=value))

# Literal string interpolation a.k.a f-strings
print(f"the value is {value}")

import datetime
print(f"The current time is {datetime.datetime.now().isoformat()}")

print(f"Math constants: pi={math.pi},e={math.e}")
print(f"Math constants: pi={math.pi:.3f},e={math.e:.3f}")