from getpass import getpass
import instaloader


    # Get username and password
username = input("Username: ")
password = getpass("Password: ")
favorite_username = input("\nFavorite page's username: ")

    # Connect to Instagram
load = instaloader.Instaloader()
load.login(username, password)
profile = instaloader.Profile.from_username(load.context, favorite_username)

    # Read old followers list from file
old_followers = []

file = open("Followers.txt", "r")
for line in file:
    old_followers.append(line.strip())
file.close()

    # Get new followers list from Instagram
new_followers = []

for follower in profile.get_followers():
    new_followers.append(follower.username)

    # Compare new followers and old followers and print new follower's username
for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

    # Write new followers list in file
file = open("Followers.txt", "w")
for new_follower in new_followers:
    file.write(new_follower + "\n")
file.close()