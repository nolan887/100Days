# Create a letter using starting_letter.pages
    # for each name in invited_names.txt
    # Replace the [name] placeholder with the actual name.
    # Save the letters in the folder "ReadyToSend".


START_LINK = "./Input/Letters/starting_letter.txt"
NAMES_LINK = "./Input/Names/invited_names.txt"
OUTPUT_LINK = "./Output/ReadyToSend/"
PLACEHOLDER = "[name]"

invited_names = []
invite_save_files = []

with open(NAMES_LINK) as f_invited:
    invited = f_invited.readlines()

for person in invited:
    invited_names.append(person.strip())

for name in invited_names:
    invite_save_files.append(name + ".txt")

with open(START_LINK, "rt") as f_start:
    letter_contents = f_start.read()
    for name in invited_names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open((OUTPUT_LINK + name + "_invite.txt"), mode="w") as completed_letter:
            completed_letter.write(new_letter)

