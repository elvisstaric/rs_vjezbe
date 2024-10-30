#printanje
print("Hello world")

# varijable
a=5

print(type(a))

b=int(input("Unesi vrijednost:"))

print(b)
print("a+b", a+b)

if bool(""):
    print("da")
else:
    print("ne")

#operatori identiteta - is ; is not


a=[1, 2, 3]

b=[1, 2, 3]

print(a is b) #ne provjerava vrijednosti nego radi li se o istoj varijabli (adresa u memoriji) -> false

b=a

print(a is b) # true

#operatori pripadnosti - in ; not in - pripadnost elemenata nekoj kolekciji



