name = input("What is your name? ")
print("Hello " + name)
print("Did you know that your name has " + str(len(name)) + " letters in it?")

# 🧠 New Concepts:
# ✅ len(name)
# Returns the number of characters in the string "Suleyman" → 8

# Like measuring how long your name is with a ruler 📏

# ✅ str()
# Converts a number (like 8) into a string so it can be joined with other text

# Like turning a number into a word so Python can read it aloud

# ⚠️ Why str() is Needed:
# You can't do:

# "letters: " + 8 ❌

# Python will throw an error:

# You can't mix strings and numbers directly.

# So you do:

# "letters: " + str(8) ✅
