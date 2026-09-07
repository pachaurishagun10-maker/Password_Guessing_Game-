import random 
 
easy_words = ["apple" , "banana" , "flame" , "cloud", "lemon" , "shark"] 
medium_words = ["bamboo" , "dragon" , "guitar" , "aeroplane" , "jungle" , "pyramid"] 
hard_words = ["astronaut" , "bizare" , "pneumonia" , "gramophone" , "monopoly" , "manifestation"] 
 
print("WELCOME TO THE PASSWORD GUESSING GAME!") 
print("You can choose difficulty level: Easy , Medium , Hard") 
difficulty_level = input("Please enter your difficulty level:").lower() 
 
if difficulty_level == "easy": 
    word = random.choice(easy_words) 
elif difficulty_level == "medium":   
    word = random.choice(medium_words) 
elif difficulty_level == "hard": 
    word = random.choice(hard_words) 
else: 
    print("Invalid choice. Reverting to easy level.") 
    word = random.choice(easy_words) 
 
attempts = 0

high_score_file = "high_score.txt"

try:
    file = open(high_score_file, "r")
    high_score = int(file.read())
    file.close()
except:
    high_score = 0
 
print("\nGuess the password! You have 5 attempts to guess.") 
 
while attempts < 5: 
    guess = input("Enter your guess: ").lower() 
    attempts += 1 
 
    if guess == word: 
        score = 6 - attempts

        print(f"Congratulations! You've guessed the password '{word}' in {attempts} attempts.")
        print(f"Your score: {score}")

        if score > high_score:
            print("New High Score!")

            file = open(high_score_file, "w")
            file.write(str(score))
            file.close()

        break 
 
    hint = "" 
 
    for i in range(len(word)): 
        if i < len(guess) and guess[i] == word[i]: 
            hint += guess[i] 
        else: 
            hint += "_" 
 
    print(f"Hint: {hint}")

if attempts == 5 and guess != word:
    print(f"\nYou ran out of attempts! The password was '{word}'.")
    print(f"High Score: {high_score}")
 
print("Game Over. Thank you for playing!")