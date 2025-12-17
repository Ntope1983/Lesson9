#Print String inside the text upper
quote = "I don't hate them...I just feel better when they're not around."
# string_input=input("Δώσε μία λέξη να μετατραπεί σε κεφαλαία")
pos = -1
string_input="0"
while string_input != "quit":
    string_input = input("Δώσε μία λέξη να μετατραπεί σε κεφαλαία")
    new_string_input = string_input.upper()
    count = quote.count(string_input)
    print(quote.replace(string_input, new_string_input, count))
