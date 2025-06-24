import random

easy = ["apple", "banana", "cherry", "tiger", "time", "mango"]
medium = ["python", "django", "flask", "hello", "dance", "temple"]
hard = ["elephant", "rabbit", "diamond", "computer", "laptop", "mountain"]

print("Welcome to Guess Game!")
print("Choose your difficulty level: easy, medium, or hard.")

level = input("Enter: ").lower()

if level == "easy":
    secret = random.choice(easy)
elif level == "medium":
    secret = random.choice(medium)
elif level == "hard":
    secret = random.choice(hard)
else:
    print("Invalid choice. You are now in easy difficulty level.")
    secret = random.choice(easy)

attempts = 0
max_attempts = 6
won = False

print("\nGuess the secret Word! You have 6 attempts.")

while attempts < max_attempts:
    guess = input(f"Attempt {attempts+1}/{max_attempts} - Guess the Word: ").lower()
    attempts += 1

    if guess == secret:
        print(f"\n🎉 You Won! The secret was '{secret}'. It took you {attempts} attempts.")
        won = True
        break
    else:
        # Generate hint
        hint = ""
        for i in range(len(secret)):
            if i < len(guess) and guess[i] == secret[i]:
                hint += guess[i]
            else:
                hint += "_"
        print("❌ Wrong guess. Hint:", hint)

if not won:
    print(f"\n💀 You've used all {max_attempts} attempts. The secret word was: '{secret}'. Better luck next time!")
