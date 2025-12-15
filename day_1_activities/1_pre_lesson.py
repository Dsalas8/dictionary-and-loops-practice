# this is what we will use for the video intro to dictionaries
#dicitonary = a collection of {key:value} pairs
            #ordered and changable. No duplicates 
capitals = {"USA": "Washington D.C.",               #Colons give the country the value of the capital, exactly like that.
            "India":"New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
#print(dir(capitals))
#print(help(capitals))
print(capitals.get("USA"))
if capitals.get("Japan"):
    print("That capital exsists")
else:
    print("That capital doesnt exsist")
capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
keys = capitals.keys()
print(capitals)
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")