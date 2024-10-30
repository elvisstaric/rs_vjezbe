a=float(input("Unesi prvi broj "))
op=(input("Unesi operator "))
b=float(input("Unesi drugi broj "))

operatori=["+", "-", "/", "*"]
if op not in operatori:
    print("Nepodržan operator")
elif b==0:
    print("Dijeljenje s nulom nije dozvoljeno!")
elif op=="+":
    print(f"Rezultat operacije  {a}{op}{b}={a+b}")
elif op=="-":
    print(f"Rezultat operacije  {a}{op}{b}={a-b}")
elif op=="*":
    print(f"Rezultat operacije  {a}{op}{b}={a*b}")
elif op=="/":
    print(f"Rezultat operacije  {a}{op}{b}={a/b}")