with open('Inputs/names.txt') as names:
    names_list = names.readlines()

for person in names_list:
    txt = 'Dear [name],\nYou are invited to my birthday this Saturday.\nHope you can make it!'
    final_letter = txt.replace('[name]',person.strip())

    with open(f'Outputs/letter_for_{person}.txt',mode='w') as letter:
        letter.write(final_letter)


