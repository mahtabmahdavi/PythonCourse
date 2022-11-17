sum = 0
score_counter = 0

while True:
    score = input("Enter a score or type 'exit': ")

    if score == "exit":
        break

    else:
        sum += float(score)
        score_counter += 1

print(f"\nYour average =", round(sum / score_counter, 2))