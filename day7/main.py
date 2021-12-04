from art import logo

alphabet = ['a', 'b', 'c', 'd',' ', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(selection,shift,start_text):
    end_text = ''
    if selection == 'decode':
        shift *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text = end_text + alphabet[new_position]
            
    return end_text

print(logo)

should_end = False

while not should_end:
    selection = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    shift = int(input("Type the shift number: "))
    text = input('Type your message: ').lower()
    print(caesar(selection,shift,text))

    if input("Type 'yes' if you want to go again. Otherwise type 'no': ") == 'no':
        should_end = True

print("Good bye")

