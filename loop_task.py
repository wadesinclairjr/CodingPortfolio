# Mini-task: Loop Feature Access
# Mini-task: Loop Feature Access
def check_access(features, role, is_logged_in):
    for feature in features:
        if is_logged_in and role == "admin":
            print(f"{feature} access granted: Admin panel.")
        elif is_logged_in:
            print(f"{feature} access granted: User view.")
        else:
            print(f"{feature} access denied: Please log in.")

# Define features list once
features = ["chat system", "blog system", "login"]

# Test case 1: role = "user", is_logged_in = True
print("Test case 1: User, logged in")
check_access(features, "user", True)

# Test case 2: role = "admin", is_logged_in = True
print("\nTest case 2: Admin, logged in")
check_access(features, "admin", True)

# Test case 3: role = "user", is_logged_in = False
print("\nTest case 3: User, not logged in")
check_access(features, "user", False)