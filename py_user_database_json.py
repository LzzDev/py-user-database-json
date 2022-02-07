import user


username = "callum"
password = "test123"


print("There are", len(user.getAll()), "users registered")

userExists = user.checkCredentials(username, password)
print("User", username, userExists and "exists" or "does not exist")

if userExists:
    user = user.getUser(username)
    print("user", user)
    print("username", user["username"])
    print("password", user["password"])
else:
    user.createUser(username, password)
    print("Created user", username, "with password", password)

    newUserExists = user.checkCredentials(username, password)
    print("[AFTER CREATE] User", username, newUserExists and "exists" or "does not exist")
    print("[AFTER CREATE] user", user.getUser(username))
