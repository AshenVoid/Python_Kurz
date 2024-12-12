string1 = input("Insert first sentence to compare: ")
string2 = input("Insert second sentence to compare: ")

#Simple if statement comparing the bool value of two strings, returning outcomes.
if len(string1) > len(string2):
    print(f"I see, the first sentence is longer, its length is: {len(string1)}.")
else:
    print(f"Hmm, curious, the second one is longer, its length is: {len(string2)}.")