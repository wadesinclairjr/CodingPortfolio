feature = "chat system"
role = "admin"
is_logged_in = True
if is_logged_in and role == "admin":
    print(f"{feature} Access granted: Admin panel.")
elif is_logged_in:
    print(f"{feature} Access granted: User view.")
else:
    print(f"{feature} Access denied: Please log in.")