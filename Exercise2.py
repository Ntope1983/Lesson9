#Count the char of the String  using dictionary
string = "I guess the only time most people think about in justice is when it happens to them."
dictionary_string={}
for char in string:
    if char.isalpha() and char.isascii():
        dictionary_string[char]=dictionary_string.get(char,0)+1
print(sorted(dictionary_string.items()))