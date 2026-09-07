import random

easy_words = ["apple" , "banana" , "flame" , "cloud", "lemon" , "shark"]
medium_words = ["bamboo" , "dragon" , "guitar" , "aeroplane" , "jungle" , "pyramid"]
hard_words = ["astronaut" , "bizzare" , "pneumonia" , "gramophone" , "monopoly" , "manifestation"]

print("WELCOME TO THE PASSWORD GUESSING GAME!")
print("You can choose difficulty level: Easy , Medium , Hard")
difficulty_level = input( "Please enter your difficulty level:").lower()

if difficulty_level == "easy":
    word = random.choice(easy_words)
elif difficulty_level == "medium":  
    word = random.choice(medium_words)
elif difficulty_level == "hard":
    word = random.choice(hard_words)
else:
    print("Invalid choice. Reverting to easy level.")
    word = random.choice(easy_words)

attempts=0
print("\nGuess the password! You have 5 attempts to guess.")
