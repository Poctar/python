vowels = ['a', 'e', 'i', 'o', 'u']

text = input("Input: ")

print("Output: ", end="")
for c in text:
    if c.lower() not in vowels:
        print(c, end="")
print()
