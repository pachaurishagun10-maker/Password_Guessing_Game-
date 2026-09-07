# Password Guessing Game--

A simple beginner-friendly Python game where the player tries to guess a randomly selected password based on the chosen difficulty level.

The game includes three difficulty levels, hints, a 5-attempt limit, and a high-score system.

# Features

- Easy, Medium, and Hard difficulty levels
- Random password selection
- Maximum of 5 attempts
- Hints after an incorrect guess
- Score system based on the number of attempts
- High score is saved permanently using a text file
- Invalid difficulty automatically switches to Easy
- Beginner-friendly Python project

# Difficulty Levels

# Easy

Easy level words such as:

- apple
- banana
- flame
- cloud
- lemon
- shark

# Medium

Medium level words such as:

- bamboo
- dragon
- guitar
- aeroplane
- jungle
- pyramid

# Hard

Hard level words such as:

- astronaut
- bizare
- pneumonia
- gramophone
- monopoly
- manifestation

# Scoring System

The player gets a higher score for guessing the password in fewer attempts.

If the player's score is higher than the previous high score, the new score is automatically saved.

# Hint System

After an incorrect guess, the game provides a hint.

The hint shows the letters that are in the correct position and replaces other letters with `_`.

For example:

```text
Password: apple
Guess:    ample
Hint:     a__le
