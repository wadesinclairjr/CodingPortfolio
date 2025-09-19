# Week 1 Small Lab Project: Form Validator.
# Build a web form validator that processes a list of form fields and thier values.

    # Use a 'for' loop to validate each field based on:
        # Username: Must not be empty and must at least 3 characters long.
        # Email: Must not be empty and must contain "@".
        # Password: Must not be empty and must be at least 6 characters long.
        # Age: Must not be empty and must be a number between 18 and 120 (use 'str.isdigit()' to check if it's a number).

    #For each field, print:
        # If valid: "[field] is valid."
        # If invalid: "[field] is invalid: [reason]."

    # Test with at least 1 invalid value.

fields = ["username", "email", "password", "age"] # List of form fields to validate
Test_cases = [ # List of test cases with different values
    ["test123", "test123@example.com", "abc123", "25"],  # All valid
    ["", "", "", ""],  # All empty
    ["", "test123example.com", "abc", "17"],  # All invalid
    ["test123", "", "abcdef", "@"],  # Mixed validity
]
for i, values in enumerate(Test_cases, 1): # Loop through each test case with index
    print(f"Test case {i}:") # Print test case header
    for field, value in zip(fields, values): # Loop through each field and its corresponding value
        if field == "username": # Validate username
            if value == "": # Check if empty
                reason = "Empty" # Reason for invalidity
                print(f"{field} is invalid: {reason}.") # Print invalid message
            elif len(value) < 3: # Check length
                reason = "Too short"
                print(f"{field} is invalid: {reason}.")
            else: # Valid case
                print(f"{field} is valid.") # Print valid message
        elif field == "email": # Validate email
            if value == "":
                reason = "Empty"
                print(f"{field} is invalid: {reason}.")
            elif "@" not in value: # Check for "@" symbol
                reason = "Missing @"
                print(f"{field} is invalid: {reason}.")
            else:
                print(f"{field} is valid.")
        elif field == "password": # Validate password
            if value == "":
                reason = "Empty"
                print(f"{field} is invalid: {reason}.")
            elif len(value) < 6:
                reason = "Too short"
                print(f"{field} is invalid: {reason}.")
            else:
                print(f"{field} is valid.")
        elif field == "age": # Validate age
            if value == "":
                reason = "Empty"
                print(f"{field} is invalid: {reason}.")
            elif not value.isdigit(): # Check if numeric
                reason = "Not a number"
                print(f"{field} is invalid: {reason}.")
            else:
                try:
                    age = int(value) # Convert to integer
                    if not (18 <= age <= 120): # Check range
                        reason = "Out of range"
                        print(f"{field} is invalid: {reason}.")
                    else:
                        print(f"{field} is valid.")
                except ValueError: # Handle conversion error
                    reason = "Not a number"
                    print(f"{field} is invalid: {reason}.")



# Output:
# Test case 1:
# username is valid.
# email is valid.
# password is valid.
# age is valid.
# Test case 2:
# username is invalid: Empty.
# email is invalid: Empty.
# password is invalid: Empty.
# age is invalid: Empty.
# Test case 3:
# username is invalid: Empty.
# email is invalid: Missing @.
# password is invalid: Too short.
# age is invalid: Out of range.
# Test case 4:
# username is valid.
# email is invalid: Empty.
# password is valid.
# age is invalid: Not a number.

# Note: The output will vary based on the test cases provided.

# End of the lab project.