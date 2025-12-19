user = {"id": 1}
x = user.get("email")
print(x)
x = user.get("key", "Default")
print(user["email"])