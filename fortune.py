# fortune.py

def main():
    name = "Aditya Dubey"
    admission_number = "20JE0056"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print(f"✨ Your fortune: Great things await you, {name}! Keep smiling. ✨")
    elif mood == "sad":
        print("💫 Your fortune: Storms don’t last forever. Better days are coming.")
    elif mood == "neutral":
        print("🌟 Your fortune: A surprise is waiting around the corner.")
    elif mood == "stressed":
        print("🌈 Your fortune: Take a deep breath. Everything will be okay.")
    else:
        print("🤔 Mood not recognized. Try happy, sad, or neutral.")

if __name__ == "__main__":
    main()
