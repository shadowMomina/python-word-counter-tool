# 📝 Word Counter Tool
# Day 24 of 90 Days Python Series
# Author: Momina Raheel

# This program counts the number of words, characters, and sentences in a given text.
# It keeps running until the user decides to quit.

print("✨ Welcome to the Word Counter Tool ✨")

while True:
    # Take input from the user
    text = input("\nEnter your text or paragraph:\n")

    # Remove extra spaces
    cleaned_text = text.strip()

    # Count words (split by spaces)
    words = cleaned_text.split()
    word_count = len(words)

    # Count characters (excluding spaces)
    char_count = len(cleaned_text.replace(" ", ""))

    # Count sentences (split by '.', '!', '?')
    sentence_count = 0
    for ch in cleaned_text:
        if ch in ".!?":
            sentence_count += 1

    # Display results
    print("\n📊 Your Text Summary 📊")
    print(f"Words: {word_count}")
    print(f"Characters (without spaces): {char_count}")
    print(f"Sentences: {sentence_count}")

    # Ask if the user wants to analyze more text
    choice = input("\nDo you want to analyze another text? (yes/no): ").lower()

    # Break loop if user chooses 'no'
    if choice != "yes":
        print("\nThanks for using the Word Counter Tool! 🧡")
        break
