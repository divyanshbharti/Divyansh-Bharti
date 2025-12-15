"""
Mad Libs Game
A simple word game where the user fills in blanks to create a funny story.
"""

def madlibs():
    adjective1 = input("Enter an adjective (description): ")
    noun1 = input("Enter a noun (person, place, or thing): ")
    adjective2 = input("Enter an adjective (description): ")
    verb1 = input("Enter a verb ending with 'ing': ")
    adjective3 = input("Enter an adjective (description): ")

    print("\n--- Your Mad Libs Story ---\n")
    print(f"Today I went to a {adjective1} zoo.")
    print(f"In an exhibit, I saw a {noun1}.")
    print(f"The {noun1} was {adjective2} and {verb1}.")
    print(f"I was {adjective3}.")

if __name__ == "__main__":
    madlibs()
