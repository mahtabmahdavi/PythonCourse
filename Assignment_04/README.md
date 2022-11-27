# Instagram New Followers Finder

This is a program which is written in **python** language.

You can see list of people who have recently followed your account or another public account by using it.

First, for running this program, you need to install [instaloader](https://instaloader.github.io/) library. You can install it with the following command:
```
pip install instaloader
```
---
## How does this program work?
At the beginning, your username and password will be taken to connect to your Instagram account. Then you enter the username of your desired account.

In the first run of this program, followers list is taken and stored in a file with the extension **"txt"**.

In the next executions, old followers list is read from our file and after receiving followers list from Instagram, these two lists are compared with each other to find new followers and print their username.
At the end, we update followers list and save it in our file.