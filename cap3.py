import os  # Import the os module to interact with the operating system

def extract_number(line):
    # Function to extract a two-digit number from a line
    # The number is formed by the first and last digits found in the line
    
    first_digit = None  # Initialize the first digit to None
    for char in line:  # Iterate over each character in the line
        if char.isdigit():  # Check if the character is a digit
            first_digit = char  # Assign the first digit
            break  # Break the loop after finding the first digit
    
    last_digit = None  # Initialize the last digit to None
    for char in reversed(line):  # Iterate over each character in the reversed line
        if char.isdigit():  # Check if the character is a digit
            last_digit = char  # Assign the last digit
            break  # Break the loop after finding the last digit

    if first_digit is not None and last_digit is not None:
        # If both digits are found, concatenate them into a string, convert to integer, and return
        return int(first_digit + last_digit)
    return 0  # Return 0 if either digit is not found

def calculate_sum_from_file(file_path):
    # Function to calculate the sum of two-digit numbers extracted from each line of a file
    
    total_sum = 0  # Initialize the total sum to 0
    with open(file_path, 'r') as file:  # Open the file at file_path in read mode
        for line in file:  # Iterate over each line in the file
            line = line.strip()  # Remove any leading/trailing whitespace from the line
            number = extract_number(line)  # Extract the two-digit number from the line
            total_sum += number  # Add the extracted number to the total sum
    return total_sum  # Return the total sum after processing all lines

# Define the path to the file
file_path = '318.txt'  # Update this path if the file is in a different location

# Check if the file exists at the specified path
if not os.path.exists(file_path):  # If the file does not exist
    print(f"File not found: {file_path}")  # Print an error message
else:  # If the file exists
    result = calculate_sum_from_file(file_path)  # Calculate the sum from the file
    print("The total sum is:", result)  # Print the result


## REFERENCES
#https://docs.python.org/3/library/os.html
#https://www.geeksforgeeks.org/reading-writing-text-files-python/
#https://www.geeksforgeeks.org/python-extract-numbers-from-string/
#https://docs.python.org/3/library/stdtypes.html#str.isdigit
#https://www.python.org/

# Run the solution
#file_name = '318.txt'#assigns the filename '318.txt' to the variable file_name, which will be used to reference the input file during the program execution.
#print_solution(file_name)#It calls the function print_solution() with the argument file_name, which triggers the printing of the total sum of two-digit numbers extracted from the specified input file.

#The solution number is:
#488403