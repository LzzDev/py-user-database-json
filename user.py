import json

def openDatabase(mode):
    if not mode == "r" and not mode == "w": # read (r) or write (w)
        return None

    try:
        db = open("users.json", mode)

        if mode == "r":
            data = db.read()
            db.close()
            return data
        else:
            return db
    except:
        return None

def readDatabase():
    db = openDatabase("r")
    return json.loads(db)

def writeDatabase(contents):
    db = openDatabase("w")
    json.dump(contents, db)
    db.close()

# Get all users
def getAll():
    return readDatabase()

# Get a user by username
def getUser(username):
    for user in readDatabase():
        if user and user["username"] == username:
            return user

    return None

# Create a user
def createUser(username, password):
    users = getAll()
    users.append({
        "username": username,
        "password": password
    })

    writeDatabase(users)

# Check if input credentials are registered
def checkCredentials(username, password):
    user = getUser(username)
    if user and user["password"] == password:
        return True

    return False