# find string in the poem (part of the word!!).In which row and print the poem with the find str in uppercase
poem = """ There’s a bluebird in my heart that
wants to get out
but I’m too tough for him,
I say,
stay down, do you want to mess me up?
you want to screw up the works?
you want to blow my book sales in Europe?
"""


while True:
    poem_lowered = poem.lower()
    list_poem_lines = poem.splitlines()
    string_input = input("Δώσε μία λέξη για αναζήτηση")
    if string_input == "quit":
        break
    for index in range(len(list_poem_lines)):
        if list_poem_lines[index].find(string_input) != -1:
            print(f"The word {string_input} find in Row: {index+1}")
            list_poem_lines[index]=list_poem_lines[index].replace(string_input,string_input.upper())
    for pos in list_poem_lines:
        print(str(pos))