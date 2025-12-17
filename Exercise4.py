# Practise with some String function strip,isalpha
def correct_name(x):
    y = x[0].upper()
    y = y + x[1:].lower()
    return y


while True:
    name = input("Give a name")
    surname = input("Give a surname")
    if name.isalpha() and surname.isalpha() and len(name) > 2 and len(surname) > 2:
        break
name=name.strip()
surname=surname.strip()
name = correct_name(name)
surname = correct_name(surname)
total_name = "Hello " + name + " " + surname
print("+" + "-" * 28 + "+")
print("|".ljust(0) + total_name.center(28) + "|".rjust(0))
print("+" + "-" * 28 + "+")
