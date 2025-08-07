print("Welcome to Love Calculator!")
print("The goal is to work out the love score between two people.")

def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    combined_names = name1 + name2

    true_count = 0
    love_count = 0

    for letter in "true":
        count = combined_names.count(letter)
        true_count += count
        print(f"{letter.upper()} occurs {count} times.")

    for letter in "love":
        count = combined_names.count(letter)
        love_count += count
        print(f"{letter.upper()} occurs {count} times.")

    print(f"Total TRUE score = {true_count}")
    print(f"Total LOVE score = {love_count}")

    love_score = int(str(true_count) + str(love_count))
    print(f"Their final love score is {love_score}.")

calculate_love_score("Kanye West", "Kim Kardashian")
