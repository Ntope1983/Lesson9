string = """
How the hell could a person enjoy being awakened at 6:30AM, 
by an alarm clock, leap out of bed, dress, force-feed, shit, piss, 
brush teeth and hair, and fight traffic to get to a place 
where essentially you made lots of money for somebody else 
and were asked to be grateful for the opportunity to do so?"""

#Count the char of the String  using dictionar
dictionary_string= {}

for char in string.lower():
    if char.isalpha():
        dictionary_string[char]=dictionary_string.get(char,0)+1
print(dictionary_string)
