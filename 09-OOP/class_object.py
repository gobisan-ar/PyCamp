from prettytable import PrettyTable


class User:

    # constructor
    def __init__(self, user_id, username):
        # attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.followings = 0

    # methods
    def follow(self, user):
        user.followers += 1
        self.followings += 1


table = PrettyTable()
table.align = "l"


user_1 = User("001", "Gary")
user_2 = User("002", "Bruce")
user_1.follow(user_2)

table.add_column("ID", [user_1.id, user_2.id])
table.add_column("Name", [user_1.username, user_2.username])
table.add_column("Followers", [user_1.followers, user_2.followers])
table.add_column("Followings", [user_1.followings, user_2.followings])
print(table)

