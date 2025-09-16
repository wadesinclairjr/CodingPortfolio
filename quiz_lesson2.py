points = 45
if points > 50:
    print("Win")
else:
    print("Try again")


users = 150
is_premium = True
if users > 100:
    if is_premium:
        print("High-Traffic Premium Feature!")
    else:
        print("High-Traffic Standard Feature.")
else:
    print("Low-Traffic Feature.")