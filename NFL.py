import sys, random

print("Welcome to the NFL 'What If Name Picker.'\n")
print("Imagine If the New York Giants were the New York Rams:\n\n")

first = ('New York', 'Arizona', 'Green Bay', "Jacksonville'",
         "Charlotte'", 'Buffalo', 'Tampa Bay', "Cincinnati' ",
         'Baltimore', 'Phoenix', 'Kansas City', 'Inidanapolis', 'Cleveland',
         'Detroit', 'Atlanta', 'Miami', 'Houston', 'Dallas', 'Oakland',
         'Philadelphia', 'Los Angeles', 'Minneapolis', 'Pittsburgh', 'New Jersey',
         'Washington', 'New Engalnd', 'San Francisco', 'Chicago', 'Denver', 'Seattle',
         'Tennessee', 'New Orleans')

last = ('Cardinals', 'Falcons', 'Ravens', 'Bills',
        'Bears', 'Panthers', 'Bengals', 'Cowboys',
        'Browns', 'Broncos', 'Lions', 'Packers', 'Texans',
        'Colts', 'Jaguars', 'Chiefs', 'Dolphins', 'Vikings',
        'Patriots', 'Saints', 'Giants', 'Jets', 'Raiders',
        'Eagles', 'Steelers', "Rams", 'Chargers', '49ers', 'Seahawks',
        'Buccaneers', 'Titans', 'Redskins')

while True:

    firstName = random.choice(first)

    lastName = random.choice(last)

    print("\n\n")
    print(firstName, lastName, file = sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
