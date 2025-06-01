# pattern_drawing.py

# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print '*' size times in one line
    for col in range(size):
        print("*", end="")  # Print on the same line
    print()  # Move to the next line after each row
    row += 1  # Move to the next row
