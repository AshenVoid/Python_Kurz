
#len() looks for the number of characters starting with 0
#index() looks for specified character and returns its index value
str = input("Insert any sentence to play with it: ")
print(f'str.index(), the thing you were looking for is indexed at:  {str.index(input("What do you want to look for? "))}')
print(f"len(str), the length of this sentence (string) is: {len(str)}")
