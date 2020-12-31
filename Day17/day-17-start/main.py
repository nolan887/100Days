class User:
    def __init__(self, user_id, username):
        # initialize attributes
        self.id = user_id
        self.username = username
        # This is the default value of 0 for followers every time, does not require followers to be passed in
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1
        print(f"{self.username} is now following {self.following} people.")
        print(f"{user.username}'s following increased to {user.followers}.")



# # Code for a 'blank' User class
# user_1 = User()
# user_1.id = "007"
# user_1.username = "James"

# Code using init method in the User class
user_1 = User("001","Charles")
user_1.following = 68
user_2 = User("002","Ashley")
user_3 = User("003","Kai")
user_7 = User("007","James")

print(user_2.id)
print(user_2.username)
print(user_2.followers)

user_1.follow(user_2)
print({user_2.followers})
print(f"# of people {user_1.username} is following: {user_1.following}")
