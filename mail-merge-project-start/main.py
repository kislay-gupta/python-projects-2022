# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, striped_name)

        with open(f"Output/ReadyToSend/letter_for_{striped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
print("done")
