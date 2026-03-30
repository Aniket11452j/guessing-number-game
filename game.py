import random
import json

# ------------------ DIFFICULTY ------------------
def get_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    choice = input("Enter choice: ")

    if choice == "1":
        return 10
    elif choice == "2":
        return 50
    else:
        return 100


# ------------------ GAME LOGIC ------------------
def play_game(max_range):
    bot = random.randint(1, max_range)
    attempts = 0
    max_limit = 5

    while attempts < max_limit:
        try:
            guess = int(input(f"Enter number (1 to {max_range}): "))

            if guess < 1 or guess > max_range:
                print("Invalid range!")
                continue

            attempts += 1

            if guess > bot:
                print("Too high 📈")
            elif guess < bot:
                print("Too low 📉")
            else:
                print(f"Correct 🎉 in {attempts} attempts")
                return attempts

        except ValueError:
            print("Enter numbers only!")

    print(f"Game Over 😢 | Number was {bot}")
    return None


# ------------------ HIGH SCORE ------------------
def load_high_score():
    try:
        with open("highscore.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_high_score(data):
    with open("highscore.json", "w") as file:
        json.dump(data, file)


# ------------------ LEADERBOARD ------------------
def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_leaderboard(data):
    with open("leaderboard.json", "w") as file:
        json.dump(data, file)


def update_leaderboard(name, score, difficulty):
    leaderboard = load_leaderboard()

    leaderboard.append({
        "name": name,
        "score": score,
        "difficulty": difficulty
    })

    # sort by score (lowest attempts = best)
    leaderboard.sort(key=lambda x: x["score"])

    save_leaderboard(leaderboard)

    print("\n🏆 Top 5 Leaderboard:")
    for i, player in enumerate(leaderboard[:5], start=1):
        print(f"{i}. {player['name']} - {player['score']} ({player['difficulty']})")


# ------------------ MAIN ------------------
def main():
    print("="*30)
    print("🎮 NUMBER GUESSING GAME")
    print("="*30)

    name = input("Enter your name: ")
    high_scores = load_high_score()

    while True:
        max_range = get_difficulty()
        key = str(max_range)

        # Show high score
        if key in high_scores:
            print(f"🏆 Best Score ({max_range}): {high_scores[key]} attempts")

        result = play_game(max_range)

        if result:
            # Update high score
            if key not in high_scores or result < high_scores[key]:
                print("🔥 New High Score!")
                high_scores[key] = result
                save_high_score(high_scores)

            # Update leaderboard
            update_leaderboard(name, result, max_range)

        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing ❤️")
            break


# ------------------ RUN ------------------
main()