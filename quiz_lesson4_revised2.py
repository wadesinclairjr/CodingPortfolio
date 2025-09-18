# Question 1: Use a 'for' loop to print "Validating field x" for x from 1 to 5.
for X in range(1, 6):
    print(f"Validating field {X}")

# Question 2: Use a 'while' loop to print "Checking input X" for X from 1 to 3, stopping if X equals 2 (use 'break').
attempt = 1
max_attempts = 3
while attempt < max_attempts:
    print(f"Checking input {attempt}")
    if attempt == 2:
        break
    attempt += 1

# Question 3: Use a 'for' loop to iterate over a list 'fields = ["username", "email", "password"]' and print each field.
fields = ["username", "email", "password"]
for field in fields:
    print(field)

# Question 4: se a 'for' loop and 'if' to print "Required" for fields in 'fields = ["username", "email", "bio"]' where the field is not "bio".
fields = ["username", "email", "bio"]
for field in fields:
    if field != "bio":
        print("Required")

#Question 5: Use a 'while' loop to print numbers 0 to 4, but skipping 2 with 'continue'.
num = 0
while num < 5:
    if num == 2:
        num += 1
        continue
    print(num)
    num += 1

#Tada! I've completed the quiz!
    #Revised
    
