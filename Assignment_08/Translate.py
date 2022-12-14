import gtts


def readFromFile():
    print("Loading...")

    try:
        with open("Translate.txt", "r") as file:
            text = file.read().split("\n")
            
            for i in range(0, len(text), 2):
                WORDS.append({"English":text[i], "Persian":text[i + 1]})

        print("Loaded!")

    except FileNotFoundError:
        print("The file was NOT found!")
        exit()


def menu():
    print("\nWelcome to Mahtab's Translate!")
    print("1. Translate English to Persian")
    print("2. Translate Persian to English")
    print("3. Add a new word")
    print("4. exit")
    menuChoice = int(input("Please enter your choice --> "))

    return menuChoice


def englishToPersian():
    inputText = input("\nPlease write your text in English: ").lower()
    userSentences = inputText.split(".")
    outputText = ""

    for sentence in userSentences:
        userWords = sentence.split(" ")

        for userWord in userWords:
            for WORD in WORDS:
                if userWord == WORD["English"]:
                    outputText += WORD["Persian"] + " "
                    break
            else:
                outputText += userWord + " "

        outputText += "."

    voice = gtts.gTTS(outputText, lang = "ar", slow = False)
    voice.save("Output.mp3")
    print("Output: " + outputText)


def persianToEnglish():
    inputText = input("\nPlease write your text in Persian (For multi-part words, use - instead of space): ").lower()
    userSentences = inputText.split(".")
    outputText = ""

    for sentence in userSentences:
        userWords = sentence.split(" ")

        for userWord in userWords:
            for WORD in WORDS:
                if userWord == WORD["Persian"]:  
                    outputText += WORD["English"] + " "
                    break
            else:
                outputText += userWord + " "

        outputText += "."

    voice = gtts.gTTS(outputText, lang = "en", slow = False)
    voice.save("Output.mp3")
    print("Output: " + outputText)


def addNewWord():
    tempEnglish = input("\nEnter the word in English: ")
    tempPersian = input("Enter the word in Persian: ")
    
    if not any(WORD["English"] == tempEnglish and WORD["Persian"] == tempPersian for WORD in WORDS):
        WORDS.append({"English":tempEnglish, "Persian":tempPersian})
        print("\nThe word added successfully!\n")

        with open("Translate.txt", "a") as file:
            file.write("\n" + tempEnglish + "\n" + tempPersian)
         
    else:
        print("\nThis word is already available.\n")
        

WORDS = []
readFromFile()

while True:
    choice = menu()

    if choice == 1:
        englishToPersian()
    elif choice == 2:
        persianToEnglish()
    elif choice == 3:
        addNewWord()
    elif choice == 4:
        exit()
    else:
        print("\nThe input isn't valid.\nTry again!")