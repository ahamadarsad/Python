print("Dictionary is keys:values pair: ")
a={
    "Name": "ARSAD",
    "Age" : 20,
    "Location": "Rajapalayam",
    "Marks" : [55,48,70,55,60]
    }
print(a)

print()
print("Print key")
print(a.keys())

print()

print("Print values")
print(a.values())
print()

print("Modify a Dictionary")
a["Name"]="AHAMAD"
print(a)
print()

print("Modify a Dictionary using update() function")
a.update(
    {
        "Location":"Seithur"}
    )
print(a)
print()

print("Add a Dictionary values")
a["Fav Color"]="Aqua"
print(a)
print()

print("Delect a Dictionary using pop() function")
a.pop("Marks")
print(a)
print()

print("Empty Dictionary")
a.clear()
print(a)



