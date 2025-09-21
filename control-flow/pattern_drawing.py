# Drawing pattern with nested loops

# Getting user's input
pattern_size = int(input("Enter the size of the pattern: "))
iteration = 0
# Drawing the pattern
while iteration <= pattern_size - 1:
    for x in range(0, pattern_size):
        print("*", end="")
        
    print()
    iteration += 1 