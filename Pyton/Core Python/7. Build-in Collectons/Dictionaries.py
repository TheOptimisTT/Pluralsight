urls={"Google":"www.google.com",
      "Pluralsight":"www.plusarsight.com",
      "Sixty North":"www.sixtynorth.com",
      "Microsoft":"www.microsoft.com"}
print(urls["Pluralsight"])

#Dictionary constructor -> dict

names_and_ages=[("Alice",32),("Bob",12)]
d=dict(names_and_ages)
print(d)

phonetic = dict(a="alpha",b="beta")
print(phonetic)
print()

#Dictionary copying
#via  .copy and dict()
 
d=dict(a="alpha",b="beta")
e=d.copy()
print(e)

f=dict(e)
print(f)
print()


#Extending a dictionary
#dict.update()

f=dict(cat=1,dog=2)
print(f)
g=dict(car=3,whale=4)
print(g)
f.update(g)
print(f)

stocks ={"GOOG":891,"AAPL":416,"IBM":194}
print(stocks)
stocks.update({"GOOG":894,"YHOO":25})
print(stocks)
print()


#for-loop
colors=dict(aquamarine=1,burlywood=2,chartreus=3,cornflower=4)
print(colors)
for key in colors:
    print(f"{key} => {colors[key]}")
print()


#Values method
for value in colors.values():
    print(value)
print()


#Keys method
for key in colors.keys():
    print(key)
print()


#dict.items()
for key,value in colors.items():
    print(f"{key} => {value}")
print()


#membership test
symbols=dict(usd = 1, euro =2, BGN=3)
print("BGN" in symbols)
print("usd" not in symbols)
print()


#removing elements
#del
z={"H":1,"Te":43,"Xe":54,"Fy":137}
print(z)
del z["Fy"]
print(z)
print()


#values can be modified
m={"H":[1,2,3],"He":[3,4],"Li":[6,7]}
print(m)
m["H"] +=[4,5,6,7]
print(m["H"])
m["N"]=[13,14,15]
print(m)

from pprint import pprint as pp
pp(m)