#Mini-task: Form Checker
#Store a list of form fields and their values.
#Use a 'for' loop to check each field's value:
     # If empty (""), print "[field] is required."
     # If filled, print "[field]: is valid."
#Test with at least one empty value.
fields = ["name", "age", "date_of_birth"]
test_cases = [
    ["Bob", "53", "1969-01-01"],
    ["", "", ""],
    ["Alice", "thirty", "1990-05-15"],
    ["Charlie", "25", ""]
]
for i, values in enumerate(test_cases, 1):
    print(f"Test case {i}: {values}")
    for field, value in zip(fields, values):
        if value == "":
            print(f"{field} is required.")
        else:
            print(f"{field}: is valid.")

# Output:
# Test case 1: ['Bob', '53', '1969-01-01']
# name: is valid.
# age: is valid.
# date_of_birth: is valid.
# Test case 2: ['', '', '']
# name is required.
# age is required.
# date_of_birth is required.
# Test case 3: ['Alice', 'thirty', '1990-05-15']
# name: is valid.
# age: is valid.
# date_of_birth: is valid.
# Test case 4: ['Charlie', '25', '']
# name: is valid.
# age: is valid.
# date_of_birth is required.
# The code checks if required fields are filled and prints appropriate messages.

# End of code.