class UserDatabase:

    database = {}

    def add_user(self, username, name, email):
        self.database[email] = [name, username]

    def info(self, email):
        if email in self.database.keys():
            return self.database[email]
        else:
            return "User not registered"

    def update_info(self, email, username, name):
        if email in self.database.keys():
            self.database[email] = [name, username]


db = UserDatabase()

print(db.database)

db.add_user("test", "Test", "sghdh@gmail.com")
print(db.database)
print(db.info("sghdh@gmail.com"))
db.update_info("sghdh@gmail.com", "test2", "Test2")
print(db.database["sghdh@gmail.com"])
db.database.sort()
