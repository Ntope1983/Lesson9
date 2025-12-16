#Escape Characters practice
import random

for i in range(3):
    print("+----" * 3 + "+")
    print(f"|{random.randint(0, 999)}\t".expandtabs(5) +
          f"|{random.randint(0, 999)}\t".expandtabs(5) +
          f"|{random.randint(0, 999)}\t".expandtabs(5) + "|")

print("+----" * 3 + "+")
