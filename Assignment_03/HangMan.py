import random

words_bank = ["tree", "book", "blue", "train", "fish", "woman", "life", "freedom", "iran", "sky", "pencil", "shirt", "bicycle", "room", "jungle"]

life = 6
word = random.choice(words_bank)
user_true_chars = []

print("Welcome to HangMan Game 🎮")

while life > 0:
    flag = 1
    
    for i in range(len(word)):
        if word[i] in user_true_chars:
            print(word[i], end = " ")
        else:
            flag = 0
            print('-', end = " ")
            
    if flag == 1:
        print("\n")
        print("You win 🎉")
        break

    user_char = input("\nEnter your chosen character: ").lower()

    if len(user_char) == 1:
        if user_char in word:
            user_true_chars.append(user_char)
            print('✅')
        else:
            life -= 1
            print('❌')
    else:
        print("Enter only one character!")

if life == 0:
    print("\nGame Over 💀")
    print(f"\"{word}\"")