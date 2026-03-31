import random
 
def scramble_word(word):
    """Scramble a word, ensuring it's different from the original."""
    word_list = list(word)
    scrambled = word_list[:]
    attempts = 0
    while ''.join(scrambled) == word and attempts < 100:
        random.shuffle(scrambled)
        attempts += 1
    return ''.join(scrambled)
 
def play_game():
    print("=" * 40)
    print("       🔀 WORD SCRAMBLE GAME 🔀")
    print("=" * 40)
 
    # Get word list from user
    print("\nEnter your words separated by commas.")
    print("Example: apple, banana, mango\n")
    raw_input = input("Your words: ")
    words = [w.strip().lower() for w in raw_input.split(",") if w.strip()]
 
    if not words:
        print("No words entered. Exiting.")
        return
 
    print(f"\n✅ Got {len(words)} word(s): {', '.join(words)}")
    print("\nLet's play! Type the correct word to win.")
    print("Type 'hint' to reveal the first letter.")
    print("Type 'quit' to exit.\n")
    print("-" * 40)
 
    # Pick a random word from the list
    target_word = random.choice(words)
    scrambled = scramble_word(target_word)
 
    print(f"\n🔀 Scrambled word: {scrambled.upper()}")
    print(f"   ({len(target_word)} letters)\n")
 
    attempt = 0
 
    while True:
        guess = input("Your guess: ").strip().lower()
        attempt += 1
 
        if guess == "quit":
            print(f"\n👋 You quit! The word was: {target_word.upper()}")
            print("Thanks for playing!")
            break
 
        elif guess == "hint":
            attempt -= 1  # Don't count hint as an attempt
            print(f"💡 Hint: The word starts with '{target_word[0].upper()}'\n")
 
        elif guess == target_word:
            print("\n" + "=" * 40)
            print("  🎉 CORRECT! WELL DONE! 🎉")
            print(f"  The word was: {target_word.upper()}")
            print(f"  You got it in {attempt} attempt(s)!")
            print("=" * 40 + "\n")
            break
 
        else:
            print(f"❌ Wrong! Try again...\n")
 
if __name__ == "__main__":
    play_game()
 