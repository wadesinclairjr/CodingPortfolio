feature = "easy code"
cost = 5.99
users = 100
is_live = True
print(f"The {feature} costs ${cost:.2f}, supports {users} users, and is live: {is_live}.")
if is_live:
    print("The feature is live and ready for users!")
else:
    print("The feature is still in development.")

print(type(feature)) # Output: <class 'str'>
print(type(cost))    # Output: <class 'float'>
print(type(users))   # Output: <class 'int'>
print(type(is_live)) # Output: <class 'bool'>

