family = ("mother", "father", "sister", "brother", "sister")
print(family)

print(type(family))

first_sister = family[2]
second_sister = family[4]

print(first_sister)
print(second_sister)

try:
    family.append("me")
except AttributeError as e:
    print("Error:", e)
try:
    family.pop(3)
except AttributeError as e:
    print("Error:", e)
